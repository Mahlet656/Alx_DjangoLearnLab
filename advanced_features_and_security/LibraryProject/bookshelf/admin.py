from django.contrib import admin
from .models import Book

# Define the admin class
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters to the sidebar
    list_filter = ('publication_year', 'author')
    
    # Add a search bar to search these fields
    search_fields = ('title', 'author')

# Register your models here.
# This line connects the Book model with the BookAdmin configuration.
admin.site.register(Book, BookAdmin)
