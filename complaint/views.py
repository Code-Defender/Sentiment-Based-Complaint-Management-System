from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseForbidden
from .models import Complaint
from .forms import RegisterForm, ComplaintForm

# TextBlob Integration
try:
    from textblob import TextBlob
    HAS_TEXTBLOB = True
except ImportError:
    HAS_TEXTBLOB = False

def get_priority_and_sentiment(text):
    """
    Analyzes sentiment score of the text and returns appropriate priority & score.
    If TextBlob is not installed, falls back to Medium priority and None score.
    """
    if not HAS_TEXTBLOB:
        return 'Medium', 0.0
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Simple thresholds:
    # Polarity < -0.25 (Very negative/dissatisfied) -> High
    # Polarity between -0.25 and 0.15 (Neutral/moderate) -> Medium
    # Polarity > 0.15 (Positive/polite) -> Low
    if polarity < -0.25:
        priority = 'High'
    elif polarity <= 0.15:
        priority = 'Medium'
    else:
        priority = 'Low'
        
    return priority, polarity


# --- Authentication Views ---

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    
    return render(request, 'complaint/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'complaint/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('login')
    return redirect('dashboard')


# --- Complaint Views ---

@login_required(login_url='login')
def dashboard_view(request):
    if request.user.is_staff:
        # Admin Dashboard: see all complaints
        complaints = Complaint.objects.all()
        # Admin statistics
        pending_count = complaints.filter(status='Pending').count()
        progress_count = complaints.filter(status='In Progress').count()
        resolved_count = complaints.filter(status='Resolved').count()
        
        context = {
            'complaints': complaints,
            'pending_count': pending_count,
            'progress_count': progress_count,
            'resolved_count': resolved_count,
        }
    else:
        # Normal User Dashboard: see only own complaints
        complaints = Complaint.objects.filter(user=request.user)
        context = {
            'complaints': complaints
        }
        
    return render(request, 'complaint/dashboard.html', context)


@login_required(login_url='login')
def complaint_detail_view(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    
    # Restrict viewing unless user owns the complaint or is admin/staff
    if complaint.user != request.user and not request.user.is_staff:
        raise Http404("Complaint not found or access denied.")
        
    return render(request, 'complaint/complaint_detail.html', {'complaint': complaint})


@login_required(login_url='login')
def complaint_create_view(request):
    if request.user.is_staff:
        messages.warning(request, "Administrators cannot submit complaints.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.status = 'Pending'
            
            # Step 7 & Step 12 Logic: calculate priority and sentiment score
            priority, score = get_priority_and_sentiment(complaint.description)
            complaint.priority = priority
            complaint.sentiment_score = score
            
            complaint.save()
            messages.success(request, "Complaint submitted successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please check the form inputs.")
    else:
        form = ComplaintForm()
        
    return render(request, 'complaint/complaint_form.html', {'form': form})


@login_required(login_url='login')
def complaint_edit_view(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    
    # Only owner can edit
    if complaint.user != request.user:
        return HttpResponseForbidden("You are not authorized to edit this complaint.")
        
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            edited_complaint = form.save(commit=False)
            
            # Recalculate priority/sentiment based on updated description
            priority, score = get_priority_and_sentiment(edited_complaint.description)
            edited_complaint.priority = priority
            edited_complaint.sentiment_score = score
            
            edited_complaint.save()
            messages.success(request, "Complaint updated successfully!")
            return redirect('complaint_detail', pk=complaint.pk)
    else:
        form = ComplaintForm(instance=complaint)
        
    return render(request, 'complaint/complaint_form.html', {'form': form})


@login_required(login_url='login')
def complaint_delete_view(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    
    # Only owner can delete
    if complaint.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this complaint.")
        
    if request.method == 'POST':
        complaint.delete()
        messages.success(request, "Complaint deleted successfully.")
        return redirect('dashboard')
        
    return render(request, 'complaint/complaint_confirm_delete.html', {'complaint': complaint})


@login_required(login_url='login')
def complaint_update_status_view(request, pk):
    # Admin only
    if not request.user.is_staff:
        return HttpResponseForbidden("Unauthorized access.")
        
    if request.method == 'POST':
        complaint = get_object_or_404(Complaint, pk=pk)
        new_status = request.POST.get('status')
        if new_status in dict(Complaint.STATUS_CHOICES):
            complaint.status = new_status
            complaint.save()
            messages.success(request, f"Status of complaint #{complaint.pk} updated to {new_status}.")
        else:
            messages.error(request, "Invalid status choice.")
            
    return redirect('dashboard')
