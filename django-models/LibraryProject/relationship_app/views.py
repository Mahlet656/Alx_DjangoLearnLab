from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    """
    Retrieves all book objects from the database and renders them in a list.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to show library details
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books it contains.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
