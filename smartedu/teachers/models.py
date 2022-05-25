from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstName = models.CharField(max_length=30, verbose_name="Öğretmen Adı", help_text="Öğretmen adı giriniz", null=0, blank=0);
    lastName = models.CharField(max_length=30, verbose_name="Öğretmen Soyadı", help_text="Öğretmen soyadı giriniz", null=0, blank=0);
    jobTitle = models.CharField(max_length=45, verbose_name="Öğretmen Alanı", help_text="Öğretmen alanı giriniz", null=0, blank=0);
    image = models.ImageField(upload_to="uploads/teachers/%Y/%m/%d/", default="uploads/teachers/default.png");
    registerDate = models.DateTimeField(auto_now=1);
    facebook = models.CharField(max_length=70, blank=True, null=True, verbose_name="Facebook", help_text="Facebook adresi giriniz");
    linkedIn = models.CharField(max_length=70, blank=True, null=True, verbose_name="LinkedIn", help_text="LinkedIn adresi giriniz");
    twitter = models.CharField(max_length=70, blank=True, null=True, verbose_name="Twitter", help_text="Twitter adresi giriniz");
    skype = models.CharField(max_length=70, blank=True, null=True, verbose_name="Skype", help_text="Facebook adresi giriniz");
    def __str__(self):
        return self.firstName + " " + self.lastName;