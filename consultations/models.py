from django.db import models
from rendezvous.models import RendezVous

class Consultation(models.Model):
    rendez_vous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)
    diagnostic = models.TextField(blank=True, null=True)
    traitement = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    poids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tension_arterielle = models.CharField(max_length=20, blank=True, null=True)
    date_consultation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation du {self.date_consultation} - {self.rendez_vous.patient}"