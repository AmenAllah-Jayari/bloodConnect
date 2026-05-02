from django import forms
from django.db import models  # Importation s7i7a mta3 models
from accounts.models import Donneur

class DonneurProfileForm(forms.ModelForm):
    class Meta:
        model = Donneur
        fields = ['photo', 'ville', 'adresse', 'telephone']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre ville'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Votre adresse'}),
        }