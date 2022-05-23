# Generated by Django 4.0.4 on 2022-05-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Kurs adı giriniz', max_length=100, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=1, max_length=300, null=1)),
                ('image', models.ImageField(default='courses/images/default.png', upload_to='courses/images/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=1)),
            ],
        ),
    ]
