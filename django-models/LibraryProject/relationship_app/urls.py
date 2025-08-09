
# relationship_app/urls.py
from .views import add_book_view, edit_book_view, delete_book_view
from django.urls import path
from .views import admin_view, librarian_view, member_view
from .views import (
    list_books, # <-- Check the spelling here
    LibraryDetailView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    # Make sure the name here matches the redirect in register_view
    path('books/', list_books, name='book-list'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('book/add/', add_book_view, name='add_book'),
    path('book/<int:pk>/edit/', edit_book_view, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book_view, name='delete_book'),
]