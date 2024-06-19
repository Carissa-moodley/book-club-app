from django.shortcuts import redirect, render
from .models import Book_read, Vote, Book_next
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    '''
    View function for the websites homepage. 
    Displays all the books read so far this year.
    '''

    books = Book_read.objects.all()
    return render(request, 'home.html', {'books': books})


def about(request):
    '''
    View function for the about page of the site.
    Displays information about the book club.
    '''

    return render(request, 'about.html')


@login_required
def vote(request):
    '''
    View function for the voting page.
    Allows logged in users to vote for the next book to be read.
    '''

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book_next.objects.get(id=book_id)
        Vote.objects.create(user=request.user, book=book)
        return redirect('home')
    books = Book_next.objects.all()
    return render(request, 'vote.html', {'books': books})
