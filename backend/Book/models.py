from django.db import models
from django.contrib.auth.models import User


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


# create type of book model
class BookType(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# create book model
class Book(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    # book info without relation
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    number_of_pages = models.IntegerField(blank=False, null=False)
    weight = models.IntegerField(blank=False, null=False)
    released_year = models.DateField()
    international_standard_book_number = models.CharField(max_length=13)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    # book info with relation
    book_publisher = models.ForeignKey(BookPublisher, default=None, on_delete=models.CASCADE,
                                       related_name='book_publishers')
    book_type = models.ForeignKey(BookType, default=None, on_delete=models.CASCADE, related_name='book_types')
    book_subject = models.ForeignKey(BookSubject, default=None, on_delete=models.CASCADE, related_name='book_subjects')

    def __str__(self):
        return self.title
