# chauffeur/models.py

from django.db import models

class Chauffeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, unique=True, default='')  # Assurez-vous que ce champ existe
    numero_piece = models.CharField(max_length=100, unique=True)  # Assurez-vous que ce champ existe
    lieu_de_residence = models.CharField(max_length=255)
    nom_pere = models.CharField(max_length=100)  # Assurez-vous que ce champ existe
    nom_mere = models.CharField(max_length=100)  # Assurez-vous que ce champ existe
    photo = models.ImageField(upload_to='chauffeur_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
