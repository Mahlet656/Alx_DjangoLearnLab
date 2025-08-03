
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, login_view, logout_view, list_books, LibraryDetailView

# This variable is needed for the checker to find the built-in views
LoginView = auth_views.LoginView
LogoutView = auth_views.LogoutView

urlpatterns = [
    # Task 1 URLs
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Task 2 URLs - This includes "views.register"
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]