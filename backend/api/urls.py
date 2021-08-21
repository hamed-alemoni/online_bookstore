from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, UserViewSet, BookPublisherViewSet, BookTypeViewSet, BookSubjectViewSet, \
    EducationYearViewSet

app_name = 'api'
# create a simple router
router = routers.SimpleRouter()

# register all books urls with router
router.register(r'books', BookViewSet, basename='books')

# register all book types urls with router
router.register(r'users', BookTypeViewSet, basename='book-types')

# register all book publishers urls with router
router.register(r'users', BookPublisherViewSet, basename='book-publishers')

# register all book subjects urls with router
router.register(r'users', BookSubjectViewSet, basename='book-subjects')

# register all education year urls with router
router.register(r'users', EducationYearViewSet, basename='education-year')

# register all users urls with router
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # set all urls that register with router
    path('', include(router.urls)),
]

