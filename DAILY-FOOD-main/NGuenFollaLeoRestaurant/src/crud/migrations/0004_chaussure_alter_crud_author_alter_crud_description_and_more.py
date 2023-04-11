# Generated by Django 4.1.2 on 2022-12-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_crud1_description1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaussure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.PositiveIntegerField()),
                ('email2', models.EmailField(blank=True, max_length=254)),
                ('phone2', models.PositiveIntegerField(default='')),
                ('suject2', models.CharField(max_length=30)),
                ('description2', models.TextField(default='votre probleme')),
            ],
        ),
        migrations.AlterField(
            model_name='crud',
            name='author',
            field=models.CharField(default='NEWS', max_length=30),
        ),
        migrations.AlterField(
            model_name='crud',
            name='description',
            field=models.TextField(default='commentaire'),
        ),
        migrations.AlterField(
            model_name='crud1',
            name='author1',
            field=models.CharField(default='bien chaud', max_length=30),
        ),
    ]
