from django.db import models

class Restaurant(models.Model):
    Titre = models.CharField(max_length=50, null=True)
    Image = models.ImageField(upload_to='media' , blank=True)
    siege = models.CharField(max_length = 30, default = 'Yaounde')
    telephone = models.CharField(max_length = 30, default = '678963685')
    description = models.CharField(max_length = 40, null=True)
    Email = models.EmailField( blank=True)

    def _str_(self):
        return self.Titre

class Commentaire(models.Model):
    name2 = models.CharField(max_length=30)
    email2 = models.EmailField(blank=True)
    phone2 = models.PositiveIntegerField(default='+237')
    suject2 = models.CharField(max_length=30)
    description2 = models.TextField(default='votre probleme')

    def __str__(self):
        return self.name2

# class Crud(models.Model):
#     name = models.CharField(max_length=50)
#     picture = models.ImageField()
#     author = models.CharField(max_length=30, default='NEWS')
#     email = models.EmailField(blank=True)
#     description = models.TextField(default='commentaire')

#     def __str__(self):
#         return self.name


# class Crud1(models.Model):
#     name1 = models.CharField(max_length=50)
#     picture1 = models.ImageField()
#     author1 = models.CharField(max_length=30, default='bien chaud')
#     email1 = models.EmailField(blank=True)
#     description1 = models.PositiveIntegerField(default='0')

#     def __str__(self):
#         return self.name1