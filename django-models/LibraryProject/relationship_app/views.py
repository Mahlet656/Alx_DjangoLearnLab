from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile # Add UserProfile import
from django.contrib.auth.decorators import login_required, user_passes_test

# --- Access Check Functions for Decorators ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- New Role-Based Views ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --- Previous Views ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Default new users to Member role
            user.userprofile.role = 'Member'
            user.userprofile.save()
            login(request, user)
            return redirect('/') # Redirect to a homepage or dashboard
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # In a real application, this would render a form.
    # For this task, a simple response is enough.
    return HttpResponse("You are authorized to add a book.")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    # A placeholder view for editing a book
    return HttpResponse(f"You are authorized to edit book {book_id}.")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    # A placeholder view for deleting a book
    return HttpResponse(f"You are authorized to delete book {book_id}.")
