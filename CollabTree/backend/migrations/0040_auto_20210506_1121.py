# Generated by Django 3.2 on 2021-05-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0039_alter_project_project_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
