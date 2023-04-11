from django.shortcuts import render, redirect
from .models import Crud, Crud1,  Chaussure, Crud2
from .form import Crud1Create, CrudCreate, ChaussureForm, Crud2Create
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Chaussure


def index(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/index.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})


def problem(request):
    return render(request, 'crud/problem.html', {
        'crud': Chaussure.objects.all()
    })


def view_chaussure(request, id):
    chaussure = Chaussure.objects.get(pk=id)
    return HttpResponseRedirect(reverse('problem'))


def add(request):
    if request.method == 'POST':
        form = ChaussureForm(request.POST)
        if form.is_valid():
            new_name2 = form.cleaned_data['name2']
            new_email2 = form.cleaned_data['email2']
            new_phone2 = form.cleaned_data['phone2']
            new_suject2 = form.cleaned_data['suject2']
            new_description2 = form.cleaned_data['description2']

            new_chaussure = Chaussure(
                name2=new_name2,
                email2=new_email2,
                phone2=new_phone2,
                suject2=new_suject2,
                description2=new_description2,

            )
            new_chaussure.save()
            return render(request, 'crud/add.html', {
                'form': ChaussureForm(),
                'success': True
            })
    else:
        form = Chaussure()
    return render(request, 'crud/add.html', {
        'form': ChaussureForm()
    })


def edit(request, id):
    if request.method == 'POST':
        chaussure = Chaussure.objects.get(pk=id)
        form = ChaussureForm(request.POST, instance=chaussure)
        if form.is_valid():
            form.save()
            return render(request, 'crud/edit.html', {'form': form, 'success': True})
    else:
        chaussure = Chaussure.objects.get(pk=id)
        form = ChaussureForm(instance=chaussure)
    return render(request, 'crud/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        chaussure = Chaussure.objects.get(pk=id)
        chaussure.delete()
    return HttpResponseRedirect(reverse('problem'))


def upload(request):
    upload = CrudCreate()
    if request.method == 'POST':
        upload = CrudCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}">Reload</a> """)
    else:
        return render(request, 'crud/upload_form.html', {'upload_form': upload})


def update_crud(request, crud_id):
    crud_id = int(crud_id)
    try:
        crud_shelf = Crud.objects.get(id=crud_id)
    except Crud.DoesNotExist:
        return redirect('index')
    crud_form = CrudCreate(request.POST or None, instance=crud_shelf)
    if crud_form.is_valid():
        return redirect('index')
    return render(request, 'crud/upload_form.html', {'upload_form': crud_form})


def delete_crud(request, crud_id):
    crud_id = int(crud_id)
    try:
        crud_shelf = Crud.objects.get(id=crud_id)
    except Crud.DoesNotExist:
        return redirect('index')
    crud_shelf.delete()
    return redirect('index')


def upload2(request):
    upload = Crud1Create()
    if request.method == 'POST':
        upload = Crud1Create(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}">Reload</a> """)
    else:
        return render(request, 'crud/upload2_form.html', {'upload2_form': upload})


def update2_crud(request, crud_id1):
    crud_id1 = int(crud_id1)
    try:
        crud_shelf1 = Crud1.objects.get(id1=crud_id1)
    except Crud1.DoesNotExist:
        return redirect('index')
    crud_form = CrudCreate(request.POST or None, instance=crud_shelf)
    if crud_form.is_valid():
        return redirect('index')
    return render(request, 'crud/upload2_form.html', {'upload2_form': crud_form})


def delete_crud(request, crud_id1):
    crud_id1 = int(crud_id1)
    try:
        crud_shelf1 = Crud1.objects.get(id1=crud_id1)
    except Crud1.DoesNotExist:
        return redirect('index')
    crud_shelf1.delete()
    return redirect('index')


# pour ajouter les produit a un client

def resto(request):
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/resto.html', {'shelf2': shelf2})


def upload3(request):
    upload = Crud2Create()
    if request.method == 'POST':
        upload = Crud2Create(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('resto')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'resto'}}">Reload</a> """)
    else:
        return render(request, 'crud/upload3_form.html', {'upload3_form': upload})


def update_crud(request, crud_id2):
    crud_id2 = int(crud_id2)
    try:
        crud_shelf2 = Crud2.objects.get(id2=crud_id2)
    except Crud2.DoesNotExist:
        return redirect('resto')
    crud_form2 = CrudCreate(request.POST or None, instance=crud_shelf2)
    if crud_form2.is_valid():
        return redirect('resto')
    return render(request, 'crud/upload3_form.html', {'upload_form3': crud_form})


def delete_crud(request, crud_id2):
    crud = get_object_or_404(Item, pk=id2)
    crud.delete()
    return redirect('resto')


def cart(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/cart.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})


def index(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/index.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})


def contact(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/contact.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})


def shop(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud2.objects.all()
    return render(request, 'crud/shop.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})


def single(request):
    shelf = Crud.objects.all()
    shelf1 = Crud1.objects.all()
    shelf2 = Crud1.objects.all()
    return render(request, 'crud/single-product.html', {'shelf': shelf, 'shelf1': shelf1, 'shelf2': shelf2})
