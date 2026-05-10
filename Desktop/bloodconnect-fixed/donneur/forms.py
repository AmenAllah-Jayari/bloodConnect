from django import forms
from accounts.models import Donneur
from .models import Don


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


class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ['date_don', 'etablissement', 'notes']
        widgets = {
            'date_don': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'etablissement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'établissement"}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Remarques (facultatif)'}),
        }
