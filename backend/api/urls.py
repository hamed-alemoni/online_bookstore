from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, UserViewSet

app_name = 'api'
# create a simple router
router = routers.SimpleRouter()

# register all books urls with router
router.register(r'books', BookViewSet, basename='books')

# register all users urls with router
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # set all urls that register with router
    path('', include(router.urls)),
]


