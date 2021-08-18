from rest_framework import serializers
from Book.models import Book
from django.contrib.auth import get_user_model


# create a serializer for Book module
class BookSerializer(serializers.ModelSerializer):
    # return author's info
    def get_author_info(self, book):
        info = {
            'ID': book.author.pk,
            'Username': book.author.username
        }
        return info

    # return book publisher's info
    def get_book_publisher_info(self, book):
        info = {
            'ID': book.book_publisher.pk,
            'title': book.book_publisher.title
        }

        return info

    # return book type's info
    def get_book_type_info(self, book):
        info = {
            'ID': book.book_type.pk,
            'title': book.book_type.title
        }

        return info

    # return book subject's info
    def get_book_subject_info(self, book):
        info = {
            'ID': book.book_subject.pk,
            'title': book.book_subject.title
        }

        return info

    # set a method to return author's info
    author = serializers.SerializerMethodField('get_author_info')
    # set a method to return book publisher's info
    book_publisher = serializers.SerializerMethodField('get_book_publisher_info')
    # set a method to return book type's info
    book_type = serializers.SerializerMethodField('get_book_type_info')
    # set a method to return book subject's info
    book_subject = serializers.SerializerMethodField('get_book_subject_info')

    class Meta:
        model = Book
        fields = '__all__'


# create a serializer for User module
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
