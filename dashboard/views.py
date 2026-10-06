from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from consultations.models import Consultation


@login_required
def dashboard(request):
    aujourd_hui = timezone.now().date()

    total_rdvs = RendezVous.objects.count()
    total_consultations = Consultation.objects.count()
    rdv_today = RendezVous.objects.filter(
        date_rendez_vous=aujourd_hui
    ).count()

    # Pourcentages calculés dynamiquement
    total_activite = total_rdvs + total_consultations
    if total_activite > 0:
        rdv_percentage = round((total_rdvs / total_activite) * 100)
        consultation_percentage = 100 - rdv_percentage
    else:
        rdv_percentage = 0
        consultation_percentage = 0

    context = {
        'total_patients': Patient.objects.count(),
        'total_medecins': Medecin.objects.count(),
        'rdv_today': rdv_today,
        'total_consultations': total_consultations,
        'total_rdvs': total_rdvs,
        'rdvs_recents': RendezVous.objects.select_related(
            'patient', 'medecin'
        ).order_by('-date_rendez_vous', '-heure_rendez_vous')[:10],
        'rdv_percentage': rdv_percentage,
        'consultation_percentage': consultation_percentage,
    }
    return render(request, 'dashboard/dashboard.html', context)