# relationship_app/urls.py
# relationship_app/urls.py

from django.urls import path
# Import Django's built-in authentication views
from django.contrib.auth import views as auth_views
# Import your custom register_view
from .views import list_books, LibraryDetailView, register_view

urlpatterns = [
    # Existing URLs from Task 1
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # New URLs for Authentication
    path('register/', register_view, name='register'),
    
    # URL for Login: Use Django's built-in LoginView
    # We tell it which template to use.
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # URL for Logout: Use Django's built-in LogoutView
    # We tell it which template to use.
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]