from django.contrib import admin

from . models import Users,Post

# Register your models here.
admin.site.register(Users,Post,Location,City,State)
