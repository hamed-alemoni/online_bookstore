from django.shortcuts import render

from django.views.generic import ListView
from .models import Book


# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'online_bookstore/products.html'
    context_object_name = 'books'
