```python
retrieved_book = Book.objects.get(title="1984")
print(f"{retrieved_book.title}, {retrieved_book.author}, {retrieved_book.publication_year}")
# Expected Output: 1984, George Orwell, 1949
```
