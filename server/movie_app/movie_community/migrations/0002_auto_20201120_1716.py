# Generated by Django 3.1.3 on 2020-11-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='avg_star',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
