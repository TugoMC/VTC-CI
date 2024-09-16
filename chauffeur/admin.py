# chauffeur/admin.py

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Chauffeur, HistoriqueLicenciement

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'numero_piece', 'email', 'lieu_de_residence', 'nom_pere', 'nom_mere', 'status', 'view_details_button')
    search_fields = ('nom', 'prenom', 'numero_piece')
    list_filter = ('age', 'lieu_de_residence', 'status')
    ordering = ('nom', 'prenom')

    def view_details_button(self, obj):
        url = reverse('chauffeur_details', args=[obj.id])
        return format_html('<a class="button" href="{}">Voir Détails</a>', url)

    view_details_button.short_description = 'Voir Détails'

@admin.register(HistoriqueLicenciement)
class HistoriqueLicenciementAdmin(admin.ModelAdmin):
    list_display = ('chauffeur', 'date_licenciement')
    search_fields = ('chauffeur__nom', 'chauffeur__prenom', 'date_licenciement')
