from django.db import models


# Create your models here.
class Announcement(models.Model):
    CATEGORIES = (
        ('general', 'ทั่วไป'),
        ('department', 'กลุ่มสาระ'),
        ('academic', 'วิชาการ'),
    )
    category = models.CharField(
        max_length=300, choices=CATEGORIES, default=CATEGORIES[0])
    topic = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(blank=True, upload_to='announcement/images')


class Personnel(models.Model):
    name_title = models.CharField(blank=False, max_length=128)
    name = models.CharField(blank=False, max_length=128)
    last_name = models.CharField(blank=False, max_length=128)
    position = models.CharField(blank=False, max_length=128)
    photo = models.ImageField(blank=True, upload_to='personnel/images')
