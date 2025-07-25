from django.urls import path, include
from . import views

urlpatterns = [
    # Auth URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

    # Role-Based URLs
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # Corrected Permission-Based URLs for Books
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
