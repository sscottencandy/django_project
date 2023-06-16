from django.db import models
from django.utils import timezone
from django.core import validators


class Author(models.Model):
    authorname = models.CharField(max_length=100)
    # authorid = models.AutoField(primary_key=True) 


class User(models.Model):
    # userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    
class Toon(models.Model):
    titleid = models.CharField(primary_key=True, max_length=50)
    titlename = models.CharField(max_length=50)
    starscore = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    startdate = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    thumnail_URL = models.URLField()

    comment_user = models.ManyToManyField(User, through='Comment')


class Comment(models.Model):
    toon = models.ForeignKey(Toon, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True)
    commentid = models.AutoField(primary_key=True)
    like = models.IntegerField(null=True)
