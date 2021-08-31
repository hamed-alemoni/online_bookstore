from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from extensions.utils import jalali_converter


# Create your models here.

# create book publisher model


class BookPublisher(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


# create subject of book model
class BookSubject(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# create year of education
class EducationYear(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# create type of book model
class BookType(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# create book model
class Book(models.Model):
    # book info without relation
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    number_of_pages = models.IntegerField(blank=False, null=False)
    weight = models.IntegerField(blank=False, null=False)
    released_year = models.DateTimeField()
    international_standard_book_number = models.CharField(max_length=13)
    price = models.IntegerField(blank=False, null=False, default=None)
    status = models.BooleanField(default=False)
    amount = models.IntegerField(default=False)

    # book info with relation
    book_publisher = models.ForeignKey(BookPublisher, default=None, on_delete=models.CASCADE,
                                       related_name='book_publishers')
    book_type = models.ForeignKey(BookType, default=None, on_delete=models.CASCADE, related_name='book_types')
    book_subject = models.ForeignKey(BookSubject, default=None, on_delete=models.CASCADE, related_name='book_subjects')
    book_education_year = models.ForeignKey(EducationYear, default=None, on_delete=models.CASCADE,
                                            related_name='book_education_year')

    def __str__(self):
        return self.title

    def year(self):
        return jalali_converter(self.released_year)

    year.short_description = 'سال انتشار'

    def image_tag(self):
        return format_html(f'<img width=100 height=75 styles="border-radius: 5px;" src="{self.image.url}">')

    image_tag.short_description = 'عکس'
    image_tag.allow_tags = True
