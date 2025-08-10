
# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views

# Import all the views from your app's views.py file
from .views import (
    list_books,
    LibraryDetailView,
    register,  # Use the corrected 'register' name
    admin_view,
    librarian_view,
    member_view,
    add_book_view,
    edit_book_view,
    delete_book_view
)

urlpatterns = [
    # URLs from Task 1
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # URLs from Task 2 (Authentication)
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # URLs from Task 3 (Role-Based Access)
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # URLs from Task 4 (Custom Permissions) - CORRECTED
    path('add_book/', add_book_view, name='add_book'),
    path('edit_book/<int:pk>/', edit_book_view, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book_view, name='delete_book'),
]