from django.db import models


# Create your models here.

class HomeCarousel(models.Model):
    label = models.CharField(blank=True, max_length=50)
    description = models.CharField(blank=True, max_length=100)
    image = models.ImageField(blank=False, upload_to='carousel/images')


class Announcement(models.Model):
    topic = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(blank=True, upload_to='announcement/images')


class Personnel(models.Model):
    name_title = models.CharField(blank=False, max_length=50)
    name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    photo = models.ImageField(blank=True, upload_to='personnel/images')
