# Generated by Django 3.2 on 2021-04-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_userattribs_worth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattribs',
            name='worth',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
