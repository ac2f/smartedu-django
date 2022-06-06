from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False);
    slug = models.SlugField(max_length=50, null=False, blank=False);
    def __str__(self):
        return self.name;
    
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kurs Adı", help_text="Kurs adı giriniz");
    description = models.TextField(max_length=300, null=True, blank=True);
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True);
    image = models.ImageField(upload_to="uploads/courses/%Y/%m/%d/", default="uploads/courses/default.png");
    date = models.DateTimeField(auto_now=True);
    available = models.BooleanField(default=True);
    def __str__(self):
        return self.title;