from django.db import models


# Create your models here.

class HomeCarousel(models.Model):
    label = models.CharField(blank=True)
    description = models.CharField(blank=True)


class Announcement(models.Model):
    topic = models.CharField(blank=False)
    description = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(blank=True, upload_to="carousel-image")


class Personnel(models.Model):
    name_title = models.CharField(blank=False)
    name = models.CharField(blank=False)
    lase_name = models.CharField(blank=False)
    photo = models.ImageField(blank=True)
