

# relationship_app/views.py

from django.shortcuts import render, redirect
# Import everything needed for both custom and built-in forms/functions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from .models import Book, Library

# ... (your list_books and LibraryDetailView are here) ...

# --- User Authentication Views ---

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') # Redirect to the login page
    # Handle GET request for logout as well
    logout(request)
    return render(request, 'relationship_app/logout.html')