

from django.shortcuts import render, redirect

# These imports are needed for our custom register view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Task 1 and other views
from django.views.generic.detail import DetailView
from .models import Book, Library

# ... your list_books and LibraryDetailView are here ...

# --- User Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('book-list') # This function now works
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form}) # This function now works