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

    # New Permission-Based URLs for Books
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
