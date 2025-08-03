# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # We still need this for registration
from django.contrib.auth import login # Still need login for after registration
# ... your other view imports like DetailView, Book, Library ...

# ... your list_books and LibraryDetailView are here ...

# --- User Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# The login_view and logout_view functions have been deleted.