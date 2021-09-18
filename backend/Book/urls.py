from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
)
app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('page/<int:page>', BookListView.as_view(), name='home'),
    path('book/<slug:slug>', BookDetailView.as_view(), name='detail'),
]