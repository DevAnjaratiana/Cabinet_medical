from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['patient', 'medecin', 'date_rendez_vous', 'heure_rendez_vous', 'motif']
        widgets = {
            'date_rendez_vous': forms.DateInput(attrs={'type': 'date'}),
            'heure_rendez_vous': forms.TimeInput(attrs={'type': 'time'}),
            'motif': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'patient': 'Patient',
            'medecin': 'Médecin',
            'date_rendez_vous': 'Date du rendez-vous',
            'heure_rendez_vous': 'Heure',
            'motif': 'Motif (optionnel)',
        }