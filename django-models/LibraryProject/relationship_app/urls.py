
# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    # Only include the URLs for Task 2
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]