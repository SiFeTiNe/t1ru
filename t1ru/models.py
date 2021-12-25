from django.db import models


# Create your models here.
class Announcement(models.Model):
    CATEGORIES = (
        ('general', 'ทั่วไป'),
        ('department', 'กลุ่มสาระ'),
        ('academic', 'วิชาการ'),
    )
    category = models.CharField(
        max_length=300, choices=CATEGORIES, default=CATEGORIES[0], verbose_name="หมวดหมู่")
    topic = models.CharField(
        blank=False, max_length=100, verbose_name="หัวข้อ")
    description = models.TextField(blank=False, verbose_name="คำอธิบาย")
    pub_date = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="วันที่เผยแพร่")
    image = models.ImageField(
        blank=True, upload_to='announcement/images', verbose_name="รูปภาพ")

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "ข่าวประชาสัมพันธ์"
        verbose_name_plural = "ข่าวประชาสัมพันธ์"


class Personnel(models.Model):
    name_title = models.CharField(blank=False, max_length=128, verbose_name="คำนำหน้าชื่อ")
    name = models.CharField(blank=False, max_length=128, verbose_name="ชื่อจริง")
    last_name = models.CharField(blank=False, max_length=128, verbose_name="นามสกุล")
    position = models.CharField(blank=False, max_length=128, verbose_name="ตำแหน่ง")
    photo = models.ImageField(blank=True, upload_to='personnel/images', verbose_name="รูปประจำตัว")

    def __str__(self):
        return self.name_title + self.name + self.last_name

    class Meta:
        verbose_name = "บุคลากร"
        verbose_name_plural = "บุคลากร"
