from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Book
from django.core.paginator import Paginator


# Create your views here.

class BookListView(ListView):
    paginate_by = 12
    queryset = Book.objects.all()
    template_name = 'online_bookstore/products.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'online_bookstore/product-details.html'

