from django import forms
from .models import Consultation
from rendezvous.models import RendezVous

class ConsultationForm(forms.ModelForm):
    rendez_vous = forms.ModelChoiceField(
        queryset=RendezVous.objects.all(),
        label="Rendez-vous associé",
        empty_label="Sélectionnez un rendez-vous"
    )
    
    class Meta:
        model = Consultation
        fields = ['rendez_vous', 'diagnostic', 'traitement', 'notes', 'poids', 'tension_arterielle']