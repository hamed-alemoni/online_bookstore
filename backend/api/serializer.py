from rest_framework import serializers
from Book.models import Book
from django.contrib.auth import get_user_model


# create a serializer for Book module
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# create a serializer for User module
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
