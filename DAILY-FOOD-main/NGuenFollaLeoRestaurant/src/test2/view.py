from django.shortcuts import render

from test2.settings import BASE_DIR


def index(request):
    print(BASE_DIR)
    return render(request, 'index.html')
    
    