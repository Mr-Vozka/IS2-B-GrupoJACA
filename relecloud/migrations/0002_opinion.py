# Generated by Django 4.2.6 on 2023-10-29 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("relecloud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Opinion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("comment", models.TextField(max_length=2000)),
                ("rating", models.IntegerField()),
                (
                    "cruise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="relecloud.cruise",
                    ),
                ),
            ],
        ),
    ]