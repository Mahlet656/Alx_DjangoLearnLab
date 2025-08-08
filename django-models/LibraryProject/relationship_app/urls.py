
# relationship_app/urls.py

from django.urls import path
# This line is where the error is happening. It means Python
# cannot find the name 'list_books' inside the views.py file.
from .views import (
    list_books, # <-- Check the spelling here
    LibraryDetailView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    # Make sure the name here matches the redirect in register_view
    path('books/', list_books, name='book-list'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]