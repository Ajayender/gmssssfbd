from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Slideshow(models.Model):
    photo = models.FileField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Latestnews(models.Model):
    title = models.CharField(max_length = 200)
    photo = models.FileField(blank=True,null=True)
    caption = models.CharField(max_length = 200)
    desc  = models.TextField()
    date = models.DateTimeField(blank=True,null=True)
    pdf = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    album_logo = models.FileField()
    album_title = models.CharField(max_length = 200)

    def __str__(self):
        return self.album_title



class Staff(models.Model):
    profile_photo = models.FileField(blank=True,null=True)
    name = models.CharField(max_length = 100)
    post = models.CharField(max_length = 100,blank=True,null=True)
    subject = models.CharField(max_length = 100, default='Maths')
    def __str__(self):
        return self.name

class Hof(models.Model):
    profile_photo = models.FileField(blank=True,null=True)
    name = models.CharField(max_length = 100)
    details = models.TextField()
    link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name="photos")
    photo = models.FileField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.album.album_title  + " " + str(self.created_date)
