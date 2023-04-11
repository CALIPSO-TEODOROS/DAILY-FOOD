# Generated by Django 4.1.2 on 2022-12-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crud1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50)),
                ('picture1', models.ImageField(upload_to='')),
                ('author1', models.CharField(default='Daniel', max_length=30)),
                ('email1', models.EmailField(blank=True, max_length=254)),
                ('description1', models.TextField(default='Available in DIU')),
            ],
        ),
    ]
