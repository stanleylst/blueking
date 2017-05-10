# -*- coding: utf-8 -*-


from django.contrib import admin

# Register your models here.

from test1.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)
