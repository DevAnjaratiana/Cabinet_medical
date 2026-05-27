from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from consultations.models import Consultation
from datetime import date

@login_required
def dashboard(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_medecins': Medecin.objects.count(),
        'rdv_today': RendezVous.objects.filter(date_rendez_vous=date.today()).count(),
        'total_consultations': Consultation.objects.count(),
        'total_rdvs': RendezVous.objects.count(),
        'rdvs_recents': RendezVous.objects.select_related('patient', 'medecin').order_by('-date_rendez_vous', '-heure_rendez_vous')[:10],
        'rdv_percentage': 60,  # Tu peux calculer dynamiquement si besoin
        'consultation_percentage': 40,
    }
    return render(request, 'dashboard/dashboard.html', context)