from rest_framework import serializers
from Book.models import Book, BookSubject, BookType, BookPublisher, EducationYear
from django.contrib.auth import get_user_model


# create a serializer for Book model
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

    # return book education year's info
    def get_book_education_year(self, book):
        info = {
            'ID': book.book_education_year.pk,
            'title': book.book_education_year.title
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
    book_education_year = serializers.SerializerMethodField('get_book_education_year')

    class Meta:
        model = Book
        fields = '__all__'


# create a serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# create a serializer for Book Subject model
class BookSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubject
        fields = '__all__'


# create a serializer for Book Type model
class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'


# create a serializer for Book Publisher model
class BookPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPublisher
        fields = '__all__'


# create a serializer for Book Education Year model
class EducationYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationYear
        fields = '__all__'
