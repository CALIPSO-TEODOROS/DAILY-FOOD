# Generated by Django 4.1.2 on 2023-03-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vente', '0005_rename_commentaireclient_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
