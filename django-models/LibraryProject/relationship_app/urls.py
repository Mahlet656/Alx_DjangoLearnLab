
# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view  # Include all

urlpatterns = [
    # Task 1 views
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Task 2: Custom authentication views (REQUIRED for the check to pass)
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
