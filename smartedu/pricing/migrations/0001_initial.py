# Generated by Django 4.0.4 on 2022-06-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Başlık giriniz', max_length=50, verbose_name='Başlık')),
                ('subtitle', models.CharField(help_text='Alt başlık giriniz', max_length=50, verbose_name='Alt başlık')),
                ('description', models.TextField(help_text='Açıklama giriniz', max_length=1000, verbose_name='Açıklama')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Fiyat giriniz', max_digits=8, verbose_name='Fiyat')),
                ('rows', models.TextField(help_text='Özellikler (Yeni satıra geçmek için satır sonuna "\\n" ekleyiniz)', max_length=1000, verbose_name='Özellikler')),
            ],
        ),
    ]
