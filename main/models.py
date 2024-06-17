from django.db import models
from django.contrib.auth.models import User 


class Book_read(models.Model):
    '''This model sets up a database for Books read with fields for the 
    books title, author, date read and an image of the books cover.'''

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    read_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', blank=True, null = True)

    def __str__(self):
        return self.title

class Book_next(models.Model):
    '''This model sets up a database for books to be read next with 
    fields for the books title, author and an image for the books cover.'''

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/', blank=True, null = True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    '''This model sets up a database for the user to vote for a book to
    read for next month with fields for the user, book and date voted.'''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book_next, on_delete=models.CASCADE)
    vote_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} voted for {self.book.title}"
