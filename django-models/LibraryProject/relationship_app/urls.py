# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
# Import the RENAMED register view
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    # ... existing book and library URLs ...

    # New URLs for Authentication
    # UPDATE THIS LINE to use the renamed view 'register'
    path('register/', register, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]