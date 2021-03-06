# Generated by Django 3.2 on 2021-05-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_auto_20210512_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userattribs',
            name='service',
        ),
        migrations.AddField(
            model_name='userattribs',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, to='backend.Service'),
        ),
    ]
