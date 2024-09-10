from django.contrib import admin
from .models import HistoriqueChauffeur, Vehicule

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee', 'couleur', 'immatriculation', 'kilometrage', 'date_achat', 'chauffeur')
    search_fields = ('marque', 'modele', 'immatriculation', 'chauffeur__nom', 'chauffeur__prenom')
    list_filter = ('annee', 'couleur')
    ordering = ('marque', 'modele')



@admin.register(HistoriqueChauffeur)
class HistoriqueChauffeurAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'ancien_chauffeur', 'nouveau_chauffeur', 'date_changement')
    list_filter = ('date_changement', 'vehicule')
    search_fields = ('vehicule__immatriculation', 'ancien_chauffeur__nom', 'nouveau_chauffeur__nom')
    ordering = ('-date_changement',)