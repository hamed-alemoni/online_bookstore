from django.contrib import admin
from .models import Book, BookPublisher, BookSubject, BookType, EducationYear


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # show this attribute
    list_display = ('title', 'image', 'status', 'author', 'amount', 'slug', 'number_of_pages', 'weight', 'year',
                    'international_standard_book_number')
    # filter according to these attribute
    list_filter = ('status', 'released_year')
    # search according to these attribute
    search_fields = ('title', 'year', 'description')
    prepopulated_fields = {'slug': ('title',)}
    # ordering according to these attribute
    ordering = ['status', '-released_year']


class BookPublisherAdmin(admin.ModelAdmin):
    # show this attribute
    list_display = ('title', 'description', 'slug')
    # filter according to these attribute
    list_filter = ('title',)
    # search according to these attribute
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


class BookSubjectAndBookTypeAdminAndEducationYear(admin.ModelAdmin):
    # show this attribute
    list_display = ('title', 'slug')
    # filter according to these attribute
    list_filter = ('title',)
    # search according to these attribute
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


# register Book module
admin.site.register(Book, BookAdmin)
# register Publisher module
admin.site.register(BookPublisher, BookPublisherAdmin)
# register BookSubject module
admin.site.register(BookSubject, BookSubjectAndBookTypeAdminAndEducationYear)
# register BookType module
admin.site.register(BookType, BookSubjectAndBookTypeAdminAndEducationYear)
# register BookType module
admin.site.register(EducationYear, BookSubjectAndBookTypeAdminAndEducationYear)
