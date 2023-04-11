from django.db import models

# Create your models here.


class Crud(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='NEWS')
    email = models.EmailField(blank=True)
    description = models.TextField(default='commentaire')

    def __str__(self):
        return self.name


class Crud1(models.Model):
    name1 = models.CharField(max_length=50)
    picture1 = models.ImageField()
    author1 = models.CharField(max_length=30, default='bien chaud')
    email1 = models.EmailField(blank=True)
    description1 = models.PositiveIntegerField(default='0')

    def __str__(self):
        return self.name1


class Crud2(models.Model):
    name2 = models.CharField(max_length=50)
    picture2 = models.ImageField()
    author2 = models.CharField(max_length=30, default='bien chaud')
    email2 = models.EmailField(blank=True)
    description2 = models.PositiveIntegerField(default='0')

    def __str__(self):
        return self.name2


class Chaussure(models.Model):
    name2 = models.CharField(max_length=30)
    email2 = models.EmailField(blank=True)
    phone2 = models.PositiveIntegerField(default='')
    suject2 = models.CharField(max_length=30)
    description2 = models.TextField(default='votre probleme')

    def __str__(self):
        return f'Chaussure: (self.email2) (self.suject2)'
