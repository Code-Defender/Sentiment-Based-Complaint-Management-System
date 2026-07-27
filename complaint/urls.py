from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard & CRUD
    path('', views.dashboard_view, name='dashboard'),
    path('complaint/new/', views.complaint_create_view, name='complaint_create'),
    path('complaint/<int:pk>/', views.complaint_detail_view, name='complaint_detail'),
    path('complaint/<int:pk>/edit/', views.complaint_edit_view, name='complaint_edit'),
    path('complaint/<int:pk>/delete/', views.complaint_delete_view, name='complaint_delete'),
    
    # Admin actions
    path('complaint/<int:pk>/update-status/', views.complaint_update_status_view, name='complaint_update_status'),
]
