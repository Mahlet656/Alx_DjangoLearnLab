from django.urls import path, include
from .views import list_books, LibraryDetailView, RegisterView

urlpatterns = [
    # App-specific URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    
    # Auth URLs
    # This will automatically look for templates in 'registration/'
    path('accounts/', include('django.contrib.auth.urls')),
]
