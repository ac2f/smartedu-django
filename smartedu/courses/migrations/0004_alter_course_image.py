# Generated by Django 4.0.4 on 2022-05-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='uploads/courses/default.png', upload_to='uploads/courses/%Y/%m/%d/'),
        ),
    ]