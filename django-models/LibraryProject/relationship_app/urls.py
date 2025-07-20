from django.urls import path, include
from . import views

urlpatterns = [
    # Auth URLs from previous task
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

    # New Role-Based URLs
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),
]
