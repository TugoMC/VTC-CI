from django.db import models
from chauffeur.models import Chauffeur

class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.PositiveIntegerField()
    couleur = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=100, unique=True)
    kilometrage = models.PositiveIntegerField()
    date_achat = models.DateField()
    photo = models.ImageField(upload_to='vehicules_photos/', null=True, blank=True)
    chauffeur = models.OneToOneField(Chauffeur, on_delete=models.SET_NULL, related_name='vehicule', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_vehicule = Vehicule.objects.get(pk=self.pk)
            if old_vehicule.chauffeur != self.chauffeur:
                from .models import HistoriqueChauffeur  # Import conditionnel
                HistoriqueChauffeur.objects.create(
                    vehicule=self,
                    ancien_chauffeur=old_vehicule.chauffeur,
                    nouveau_chauffeur=self.chauffeur
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"





class HistoriqueChauffeur(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='historiques')
    ancien_chauffeur = models.ForeignKey(Chauffeur, on_delete=models.SET_NULL, null=True, blank=True, related_name='historiques_anciennes')
    nouveau_chauffeur = models.ForeignKey(Chauffeur, on_delete=models.SET_NULL, null=True, blank=True, related_name='historiques_nouveaux')
    date_changement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chauffeur changé pour {self.vehicule} de {self.ancien_chauffeur} à {self.nouveau_chauffeur} le {self.date_changement}"