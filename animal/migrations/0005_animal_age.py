# Generated by Django 3.1.1 on 2020-09-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_animal_is_sterlized'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
