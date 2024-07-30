from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre

# Create your views here.

def index(request):
    
    #Counter for tables
    book_counter = Book.objects.all().count()
    instance_counter = BookInstance.objects().all().count()
    author_counter = Author.objects().all()
    
    #Counter for books available
    available_books = BookInstance.objects.filter(status__exact='a').count
    
    context = {
        'Authors': author_counter,
        'Available books': available_books,
        'Books' : book_counter,
        'Copies': instance_counter,  
    }
    
    # Render
    return render(request, 'index.html', context=context)
    