# Generated by Django 3.1.3 on 2020-12-07 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_community', '0004_review_comment_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='checked_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
