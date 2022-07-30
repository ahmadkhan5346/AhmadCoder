from django.contrib import admin
from blog.models import BlogComment, Post

# Register your models here.

admin.site.register((BlogComment))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)