from django.contrib import admin

from my_University.models import Student, Group

admin.site.register([Student, Group])

