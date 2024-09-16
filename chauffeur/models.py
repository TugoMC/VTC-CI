# chauffeur/models.py

from django.db import models
from django.utils import timezone

class Chauffeur(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_TERMINATED = 'terminated'
    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_TERMINATED, 'Terminated'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, unique=True, default='')
    numero_piece = models.CharField(max_length=100, unique=True)
    lieu_de_residence = models.CharField(max_length=255)
    nom_pere = models.CharField(max_length=100)
    nom_mere = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='chauffeur_photos/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class HistoriqueLicenciement(models.Model):
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE, related_name="licenciements")
    date_licenciement = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.chauffeur.nom} - {self.date_licenciement.strftime('%d/%m/%Y')}"
