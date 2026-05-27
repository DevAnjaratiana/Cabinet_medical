from django.db import models
from patients.models import Patient
from medecins.models import Medecin

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_rendez_vous = models.DateField()
    heure_rendez_vous = models.TimeField()
    motif = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.nom} - {self.medecin.nom} - {self.date_rendez_vous}"