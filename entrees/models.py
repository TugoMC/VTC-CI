# entrees/models.py

from django.db import models
from chauffeur.models import Chauffeur
from vehicule.models import Vehicule

class RevenuJournalier(models.Model):
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('chauffeur', 'vehicule', 'date')

    def __str__(self):
        return f"{self.chauffeur} - {self.vehicule} - {self.date} - {self.montant}€"
