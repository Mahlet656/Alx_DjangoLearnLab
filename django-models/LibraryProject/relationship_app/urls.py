from django.urls import path
from . import views

urlpatterns = [
    # URL for the function-based view that lists all books
    path('books/', views.list_books, name='list_books'),
    
    # URL for the class-based view that shows a specific library's details
    # The <int:pk> part captures the library's ID from the URL
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
