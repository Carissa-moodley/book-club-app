from django.contrib import admin
from .models import Book_read, Book_next, Vote

# Register the Book_read class so admin can add Books read
admin.site.register(Book_read)
# Register the Book_next class so admin can add Books to read next
admin.site.register(Book_next)

