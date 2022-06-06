from django.db import models

# Create your models here.
class Pricing(models.Model):
    title = models.CharField(max_length=50, help_text="Başlık giriniz", verbose_name="Başlık", blank=False, null=False);
    subtitle = models.CharField(max_length=50, help_text="Alt başlık giriniz", verbose_name="Alt başlık");
    description = models.TextField(help_text="Açıklama giriniz", verbose_name="Açıklama", max_length=1000);
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Fiyat giriniz", verbose_name="Fiyat", default=0);
    rows = models.TextField(help_text="Özellikler (Yeni satıra geçmek için satır sonuna \"\\n\" ekleyiniz)", verbose_name="Özellikler", max_length=1000);
