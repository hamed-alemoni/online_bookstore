from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from Book.models import Book


# Create your views here.

@login_required
def home(request):
    return render(request, 'registration/home.html')


class BookListView(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    template_name = 'registration/home.html'
