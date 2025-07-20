# NOTE: This script is for documentation and is not meant to be run directly.
# It assumes you have a Django shell environment set up.

from .models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. Query all books by a specific author
# Assuming an author object exists: author_obj = Author.objects.get(name="George Orwell")
# books_by_author = Book.objects.filter(author=author_obj)

# 2. List all books in a library
# Assuming a library object exists: library_obj = Library.objects.get(name="Central Library")
# books_in_library = library_obj.books.all()

# 3. Retrieve the librarian for a library
# Assuming a library object exists: library_obj = Library.objects.get(name="Central Library")
# librarian = library_obj.librarian
# NOTE: This script is for documentation and is not meant to be run directly.
# It assumes you have a Django shell environment set up.

from .models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. Query all books by a specific author
# Assuming an author object exists: author_obj = Author.objects.get(name="George Orwell")
# books_by_author = Book.objects.filter(author=author_obj)

# 2. List all books in a library
# Assuming a library object exists: library_obj = Library.objects.get(name="Central Library")
# books_in_library = library_obj.books.all()

# 3. Retrieve the librarian for a library
# Assuming a library object exists: library_obj = Library.objects.get(name="Central Library")
# librarian = library_obj.librarian
