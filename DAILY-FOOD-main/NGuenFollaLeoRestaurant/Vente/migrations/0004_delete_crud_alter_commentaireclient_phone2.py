# Generated by Django 4.1.2 on 2023-03-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vente', '0003_crud'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Crud',
        ),
        migrations.AlterField(
            model_name='commentaireclient',
            name='phone2',
            field=models.PositiveIntegerField(default='+237'),
        ),
    ]