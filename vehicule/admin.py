# vehicules/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Vehicule, HistoriqueChauffeur

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee', 'couleur', 'immatriculation', 'kilometrage', 'date_achat', 'chauffeur', 'view_details_button')
    search_fields = ('marque', 'modele', 'immatriculation', 'chauffeur__nom', 'chauffeur__prenom')
    list_filter = ('annee', 'couleur')
    ordering = ('marque', 'modele')

    def view_details_button(self, obj):
        url = reverse('vehicule_details', args=[obj.id])
        return format_html('<a class="button" href="{}">Voir Détails</a>', url)

    view_details_button.short_description = 'Voir Détails'

@admin.register(HistoriqueChauffeur)
class HistoriqueChauffeurAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'ancien_chauffeur', 'nouveau_chauffeur', 'date_changement')
    list_filter = ('date_changement', 'vehicule')
    search_fields = ('vehicule__immatriculation', 'ancien_chauffeur__nom', 'nouveau_chauffeur__nom')
    ordering = ('-date_changement',)
