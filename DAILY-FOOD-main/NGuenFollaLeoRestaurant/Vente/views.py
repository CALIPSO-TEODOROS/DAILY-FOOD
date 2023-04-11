from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Restaurant, Commentaire
from .forms import CommentaireClientForm
# import React, { Component } form'react'
# from .forms import Crud1Create, CrudCreate, CommentaireClientForm, RestaurantForm 
# from django.http import HttpResponse, HttpResponseRedirect 
# from django.urls import reverse

# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.core.mail import send_mail, EmailMessage
# from test2 import settings
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from . tokens import generateToken

# from .models import Chaussure, Restaurant


# Create your views here.
# class FormView extends Component {
#     // Code pour importer le formulaire ici
# }

def Administration(request):
    if request.method =="POST":
    # if request.POST: //  ceci est aussi possible 
        Titre = request.POST.get('Titre')
        Image = request.POST.get('Image')
        siege = request.POST.get('siege')
        telephone = request.POST.get('telephone')
        description = request.POST.get('description')
        Email = request.POST.get('Email')
        newRestaurant = Restaurant.objects.create(Titre=Titre, Image=Image, siege=siege, telephone=telephone, description=description)
        newRestaurant.save()
        message="votre restaurant est creeer"
    Restaurant_object = Restaurant.objects.all()
    return render (request, 'Vente/administrateur.html',{'Restaurant_object': Restaurant_object})



def CommentaireClient(request):
    if request.method == 'POST':
        form = CommentaireClientForm(request.POST)
        if form.is_valid():
            new_name2 = form.cleaned_data['name2']
            new_email2 = form.cleaned_data['email2']
            new_phone2 = form.cleaned_data['phone2']
            new_suject2 = form.cleaned_data['suject2']
            new_description2 = form.cleaned_data['description2']

            new_commentaire= Commentaire(
                name2=new_name2,
                email2=new_email2,
                phone2=new_phone2,
                suject2=new_suject2,
                description2=new_description2,

            )
            new_commentaire.save()
            return render(request, 'Vente/add.html', {
                'form': CommentaireClientForm(),
                'success': True
            })
    else:
        form = CommentaireClientForm()
    return render(request, 'Vente/add.html', {
        'form': CommentaireClientForm()
    })

def Accueil(request):
    return render(request, 'Vente/index.html')


def shop(request):
    
    Restaurant_object = Restaurant.objects.all()
    Restaurant_Titre =request.GET.get('Restaurant-Titre')
    if Restaurant_Titre !=' ' and Restaurant_Titre is not None:
        Restaurant_object = Restaurant.objects.filter(titre__icontains = Restaurant_Titre)
        
    # paginator =Paginator(Restaurant_object, 4)
    # page = request.GET.get('page')
    # Restaurant_object = paginator.get_page(page)
    return render(request,'Vente/shop.html', {'Restaurant_object': Restaurant_object})

def restau(request):
    # restaurant_object = Restaurant.objects.get( id = myid )
    return render(request, 'Vente/Restaurant_propre.html')

def problem(request):
    Commentaire_objet = Commentaire.objects.all()
    return render(request, 'Vente/problem.html', {'Commentaire_objet':Commentaire_objet })

def cart(request):
    
    return render(request, 'Vente/cart.html')






def delete_Restaurant(request, id):
    elementbd= Restaurant.objects.get(pk=id)
    elementbd.delete()
    return redirect('admin')

def edit_Restaurant(request, id):
    Restaurant = Restaurant.objects.get(id=request.GET['id'])
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=Restaurant)
        if form.is_valid():
            Restaurant = form.save()
            return redirect('admin')
    else:
        form = RestaurantForm(instance=Restaurant)
    return render(request, 'Vente/administrateur.html', {'form': form})







