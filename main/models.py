from django.db import models
from django.contrib.auth.models import User 


class Book_read(models.Model):
    '''
    This model represents a book read in the book club.
    '''

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    read_date = models.DateField()
    image = models.ImageField(upload_to='book_images/', blank=True, null = True)

    def __str__(self):
        '''
        String representation of the Book_read model.
        '''
        return self.title
    

class Book_next(models.Model):
    '''
    This model represents a book that could be read next month by
    the book club.
    '''

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/', blank=True, null = True)

    def __str__(self):
        '''
        String representation of the Book_next model.
        '''
        return self.title


class Vote(models.Model):
    '''
    This model represents a vote for a book to be read next by user.
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book_next, on_delete=models.CASCADE)
    vote_date = models.DateField(auto_now_add = True)

    def __str__(self):
        '''
        String representation of the Vote model.
        '''
        return f"{self.user.username} voted for {self.book.title}"
