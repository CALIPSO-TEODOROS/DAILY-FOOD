# Generated by Django 4.1.2 on 2022-12-19 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_crud1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud1',
            name='description1',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
