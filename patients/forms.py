from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'prenom', 'date_naissance', 'telephone', 'email', 'adresse']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nom': 'Last Name',
            'prenom': 'First Name',
            'date_naissance': 'Birth Date',
            'telephone': 'Phone',
            'email': 'Email',
            'adresse': 'Address',
        }
