from django.shortcuts import redirect, render
from .models import Book_read, Vote, Book_next
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    '''This method takes the user to the websites homepage which presents
    all the books read so far this year.'''

    books = Book_read.objects.all()
    return render(request, 'home.html', {'books': books})

@login_required
def vote(request):
    '''This method lets the user vote for next months book and requires
    the user to be logged in to vote.'''

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book_next.objects.get(id=book_id)
        Vote.objects.create(user=request.user, book=book)
        return redirect('home')
    books = Book_next.objects.all()
    return render(request, 'vote.html', {'books': books})
