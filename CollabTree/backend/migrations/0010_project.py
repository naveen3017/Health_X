# Generated by Django 3.1.7 on 2021-04-06 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20210406_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('duration', models.IntegerField(blank=True)),
                ('stipend', models.IntegerField(blank=True)),
                ('assigned_user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to='backend.userattribs')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='backend.userattribs')),
            ],
        ),
    ]
