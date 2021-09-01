from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from Book.models import Book


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    template_name = 'registration/home.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'title',
        'slug',
        'description',
        'image',
        'author',
        'number_of_pages',
        'weight',
        'released_year',
        'international_standard_book_number',
        'price',
        'status',
        'amount',
        'book_publisher',
        'book_type',
        'book_subject',
        'book_education_year',

    ]
    template_name = 'registration/book_create_update.html'
