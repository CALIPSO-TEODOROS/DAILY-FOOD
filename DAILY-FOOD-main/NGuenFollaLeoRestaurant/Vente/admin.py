from django.contrib import admin
from .models import  Restaurant, Commentaire

# Register your models here.
# class AdminRestaurant(admin.ModelAdmin):
#     list_display=('Titre','Image','siege','telephone','description','Email',)   

admin.site.register(Restaurant)
admin.site.register(Commentaire)
