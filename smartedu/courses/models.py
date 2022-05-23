from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kurs Adı", help_text="Kurs adı giriniz");
    description = models.TextField(max_length=300, null=1, blank=1);
    image = models.ImageField(upload_to="courses/images/%Y/%m/%d/", default="courses/images/default.png");
    date = models.DateTimeField(auto_now=1);
    available = models.BooleanField(default=1);
    def __str__(self):
        return self.title;