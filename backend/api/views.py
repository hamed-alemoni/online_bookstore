from rest_framework.viewsets import ModelViewSet
from Book.models import Book
from django.contrib.auth import get_user_model
from .serializer import BookSerializer, UserSerializer


# Create your views here.

# create book view to update, delete, create and read data
class BookViewSet(ModelViewSet):
    # get all articles
    queryset = Book.objects.all()
    # determine serializer class
    serializer_class = BookSerializer


# create user view to read data
class UserViewSet(ModelViewSet):
    # get all articles
    queryset = get_user_model().objects.all()
    # determine serializer class
    serializer_class = UserSerializer
