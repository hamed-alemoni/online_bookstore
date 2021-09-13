from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from Book.models import Book, BookPublisher, BookSubject


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


class BookPublisherListView(LoginRequiredMixin, ListView):
    queryset = BookPublisher.objects.all()
    template_name = 'registration/book_publisher_list.html'


class BookPublisherCreateView(LoginRequiredMixin, CreateView):
    model = BookPublisher
    fields = [
        'title',
        'slug',
        'description',
    ]
    template_name = 'registration/book_publisher_create_update.html'


class BookSubjectListView(LoginRequiredMixin, ListView):
    queryset = BookSubject.objects.all()
    template_name = 'registration/book_subject_list.html'


class BookSubjectCreateView(LoginRequiredMixin, CreateView):
    model = BookSubject
    fields = [
        'title',
        'slug',
    ]
    template_name = 'registration/book_subject_create_update.html'