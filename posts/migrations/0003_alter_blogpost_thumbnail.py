# Generated by Django 5.1.3 on 2024-11-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
