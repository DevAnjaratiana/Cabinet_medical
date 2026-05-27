from django import forms
from .models import Medecin

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cardiologue, Généraliste'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 06 12 34 56 78'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: docteur@email.com'}),
        }
        labels = {
            'nom': 'Nom du médecin',
            'prenom': 'Prénom du médecin',
            'specialite': 'Spécialité médicale',
            'telephone': 'Numéro de téléphone',
            'email': 'Adresse email',
        }