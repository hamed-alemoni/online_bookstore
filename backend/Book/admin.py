from django.contrib import admin
from .models import Book, BookPublisher,BookSubject,BookType
# Register your models here.

# register Book module
admin.site.register(Book)
# register Publisher module
admin.site.register(BookPublisher)
# register BookSubject module
admin.site.register(BookSubject)
# register BookType module
admin.site.register(BookType)
