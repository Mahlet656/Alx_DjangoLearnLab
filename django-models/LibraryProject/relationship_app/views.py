# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView # Keep specific import
from .models import Book, Library
# ... your other imports ...

# ... list_books, LibraryDetailView ...

def register(request):
    # ... your register code is here ... # Keep this named 'register'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

