# CRUD Operations for Book Model

## Create
```python
Book.objects.create(
    title="Things Fall Apart",
    author="Chinua Achebe",
    publication_year=1958
)
```

## Read
```python
# Get all books
Book.objects.all()

# Get a specific book by ID
Book.objects.get(id=1)

# Filter by author
Book.objects.filter(author="Chinua Achebe")

# Filter by year
Book.objects.filter(publication_year__gt=2000)

# Order by year
Book.objects.order_by('publication_year')
```

## Update
```python
book = Book.objects.get(id=1)
book.title = "No Longer at Ease"
book.publication_year = 1960
book.save()
```

## Delete
```python
book = Book.objects.get(id=1)
book.delete()
```
