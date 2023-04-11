from django import forms
from .models import Commentaire
# from .models import Crud, Crud1, Chaussure, Restaurant



class CommentaireClientForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['name2', 'email2', 'phone2', 'suject2', 'description2']
        labels = {
            'name2': 'name2',
            'email2': 'email2',
            'phone2': 'phone2',
            'suject2': 'suject2',
            'description2': 'description2',
         }
        widgets = {
            'name2': forms.TextInput(attrs={'class': 'form-control'}),
            'email2': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone2': forms.NumberInput(attrs={'class': 'form-control'}),
            'suject2': forms.TextInput(attrs={'class': 'form-control'}),
            'description2': forms.TextInput(attrs={'class': 'form-control'}),
        }