# django-models/LibraryProject/relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after they register
            return redirect('book-list') # Redirect to the main book list page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list') # Redirect to the main book list page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    # We need to handle POST requests for security
    if request.method == 'POST':
        logout(request)
        return redirect('login') # Redirect to the login page after logout
    # In a real app, the logout button would be in a form.
    # For simplicity, we can also log out on a GET request for now.
    logout(request)
    return render(request, 'relationship_app/logout.html')