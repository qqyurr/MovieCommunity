# Generated by Django 3.1.3 on 2020-12-05 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_community', '0002_auto_20201121_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
