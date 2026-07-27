from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Complaint

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'Enter {field_name}'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Summarize the issue briefly...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a detailed description of the complaint (our sentiment engine will analyze this to assign priority)...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
