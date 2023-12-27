# Generated by Django 5.0 on 2023-12-27 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('photo', models.ImageField(upload_to='res/img/cruceros/')),
            ],
        ),
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('destinations', models.ManyToManyField(related_name='cruises', to='relecloud.destination')),
            ],
        ),
        migrations.CreateModel(
            name='InfoRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(default='', max_length=2000)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relecloud.cruise')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2000)),
                ('rating', models.IntegerField()),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='relecloud.cruise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
