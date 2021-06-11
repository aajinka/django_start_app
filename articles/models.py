from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

#from django.forms import ModelForm

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Profile(models.Model):
    user = models.OneToOneField(User, null =True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self): 
        return str(self.user)

    def get_absolute_url(self):
        return reverse('list')

class Article(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    slug = models.SlugField(max_length=20, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=255, default="uncategorized")
    likes = models.ManyToManyField(User, related_name= ("article_app"))
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self): # instance se vypisují podle title
        return self.title #+'|'+str(self.year)

    #def snippet(self): # u dlouhé textu se vypíše jen prvních 50 znaků
     #   return self.body[:50] + "..." 


    def get_absolute_url(self):
        return reverse('list')#, args=(str(self.id)))
    
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s- %s' % (self.article.title, self.name)

