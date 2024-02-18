# file: appName/admin.py

from django.contrib import admin
from project.models import * # import the tables

# Register your models here.


admin.site.register(Book)


admin.site.register(Author)