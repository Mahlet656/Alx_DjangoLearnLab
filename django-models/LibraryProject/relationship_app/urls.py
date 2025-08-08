
# relationship_app/urls.py

from django.urls import path
from .views import (
    list_books, LibraryDetailView,
    register_view, login_view, logout_view,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    # Task 1 URLs
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Task 2 URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Task 3 URLs
    path('admin-dashboard/', admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', member_view, name='member-dashboard'),
]