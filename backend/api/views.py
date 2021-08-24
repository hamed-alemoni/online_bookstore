from rest_framework.viewsets import ModelViewSet
from Book.models import Book, BookSubject, BookType, BookPublisher, EducationYear
from django.contrib.auth import get_user_model
from .serializer import BookSerializer, UserSerializer, BookSubjectSerializer, BookTypeSerializer, \
    BookPublisherSerializer, EducationYearSerializer
from .permissions import IsStaffOrReadOnly, IsSuperUser
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def permissions(self):
    if self.action in ['list']:
        # just watch the info
        permission_classes = (IsAuthenticated, IsSuperUser, IsStaffOrReadOnly)
    elif self.action in ['create', 'update', 'destroy', 'partial_update']:
        # update, create and delete
        permission_classes = (IsSuperUser,)
    else:
        # others
        permission_classes = (IsStaffOrReadOnly, IsAuthenticated)
    return [permission() for permission in permission_classes]


# create book view to update, delete, create and read data
class BookViewSet(ModelViewSet):
    # get all articles
    queryset = Book.objects.all()
    # determine serializer class
    serializer_class = BookSerializer
    # determine fields of filters
    filterset_fields = ['title', 'author', 'price', 'status', 'book_publisher__title', 'book_type__title', 'book_subject__title',
                        'book_education_year__title']

    # determine fields of search filter
    search_fields = ['title', 'author', 'book_publisher__title', 'book_type__title', 'book_subject__title',
                     'book_education_year__title']
    # determine fields of ordering
    ordering_fields = ['price', 'released_year__year', 'status']
    # default ordering
    ordering = ['-released_year__year']

    # add a new permission for this view
    def get_permissions(self):
        return permissions(self)


# create book subject view to update, delete, create and read data
class BookSubjectViewSet(ModelViewSet):
    # get all articles
    queryset = BookSubject.objects.all()
    # determine serializer class
    serializer_class = BookSubjectSerializer

    # add a new permission for this view
    def get_permissions(self):
        return permissions(self)


# create book type view to update, delete, create and read data
class BookTypeViewSet(ModelViewSet):
    # get all articles
    queryset = BookType.objects.all()
    # determine serializer class
    serializer_class = BookTypeSerializer

    # add a new permission for this view
    def get_permissions(self):
        return permissions(self)


# create book type view to update, delete, create and read data
class BookPublisherViewSet(ModelViewSet):
    # get all articles
    queryset = BookPublisher.objects.all()
    # determine serializer class
    serializer_class = BookPublisherSerializer

    # add a new permission for this view
    def get_permissions(self):
        return permissions(self)


# create education year view to update, delete, create and read data
class EducationYearViewSet(ModelViewSet):
    # get all articles
    queryset = EducationYear.objects.all()
    # determine serializer class
    serializer_class = EducationYearSerializer

    # add a new permission for this view
    def get_permissions(self):
        return permissions(self)


# create user view to read data
class UserViewSet(ModelViewSet):
    # get all articles
    queryset = get_user_model().objects.all()
    # determine serializer class
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = (IsStaffOrReadOnly,)
        else:
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]
