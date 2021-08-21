from rest_framework.viewsets import ModelViewSet
from Book.models import Book, BookSubject, BookType, BookPublisher, EducationYear
from django.contrib.auth import get_user_model
from .serializer import BookSerializer, UserSerializer, BookSubjectSerializer, BookTypeSerializer, \
    BookPublisherSerializer, EducationYearSerializer


# Create your views here.

# create book view to update, delete, create and read data
class BookViewSet(ModelViewSet):
    # get all articles
    queryset = Book.objects.all()
    # determine serializer class
    serializer_class = BookSerializer


# create book subject view to update, delete, create and read data
class BookSubjectViewSet(ModelViewSet):
    # get all articles
    queryset = BookSubject.objects.all()
    # determine serializer class
    serializer_class = BookSubjectSerializer


# create book type view to update, delete, create and read data
class BookTypeViewSet(ModelViewSet):
    # get all articles
    queryset = BookType.objects.all()
    # determine serializer class
    serializer_class = BookTypeSerializer


# create book type view to update, delete, create and read data
class BookPublisherViewSet(ModelViewSet):
    # get all articles
    queryset = BookPublisher.objects.all()
    # determine serializer class
    serializer_class = BookPublisherSerializer


# create education year view to update, delete, create and read data
class EducationYearViewSet(ModelViewSet):
    # get all articles
    queryset = EducationYear.objects.all()
    # determine serializer class
    serializer_class = EducationYearSerializer


# create user view to read data
class UserViewSet(ModelViewSet):
    # get all articles
    queryset = get_user_model().objects.all()
    # determine serializer class
    serializer_class = UserSerializer
