# For "Query all books by a specific author" task
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)


# For "List all books in a library" task
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()


# For "Retrieve the librarian for a library" task
library = Library.objects.get(name="library_name")
librarian = library.librarian
