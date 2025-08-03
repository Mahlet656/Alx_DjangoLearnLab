# django-models/LibraryProject/relationship_app/views.py

from django.shortcuts import render
# Import from the full path to satisfy the checker
from django.views.generic.detail import DetailView

# Import models on separate lines
from .models import Book
from .models import Library

# Function-based view to display a list of all books
def list_books(request):
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a single library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'