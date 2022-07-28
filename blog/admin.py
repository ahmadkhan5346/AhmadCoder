from django.contrib import admin
from blog.models import BlogComment, Post

# Register your models here.

admin.site.register((Post, BlogComment))
