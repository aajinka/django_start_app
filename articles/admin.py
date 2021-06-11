from django.contrib import admin

# Register your models here.
from . models import Article, Category, Profile, Comment

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)