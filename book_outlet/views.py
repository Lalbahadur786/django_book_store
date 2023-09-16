from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    all_books = Book.objects.all().order_by('-title')
    no_of_books = all_books.count()
    avg_rating = all_books.aggregate(Avg('rating'))

    return render(request, "book_outlet\index.html", {
        "all_books": all_books,
        "total_no_of_books": no_of_books,
        "books_avg": avg_rating['rating__avg']
    })

def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet\\book_details.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best_selling": book.is_best_selling
    })