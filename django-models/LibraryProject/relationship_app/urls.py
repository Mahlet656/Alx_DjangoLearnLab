# relationship_app/urls.py

from django.urls import path
# Import all our custom views
from .views import (
    list_books,
    LibraryDetailView,
    register, # Use our renamed register
    login_view, # Use our custom login_view
    logout_view # Use our custom logout_view
)

urlpatterns = [
    # ... existing book and library URLs ...

    # New URLs for Authentication
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]