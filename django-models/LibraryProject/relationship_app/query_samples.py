
# For "Query all books by a specific author" task
Book.objects.filter(author__name="author_name")

# For "List all books in a library" task
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# For "Retrieve the librarian for a library" task
library = Library.objects.get(name__exact="library_name")
librarian_of_library = library.librarian
