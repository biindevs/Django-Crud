from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Book

#Display the books
def index(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'index_book.html', {'books': books})
#View the books
def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

# Edit the books
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'pub_date']
    template_name = 'book_edit.html'
    success_url = reverse_lazy('index')

# Delete the book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('index')
