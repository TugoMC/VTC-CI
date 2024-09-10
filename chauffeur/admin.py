from django.contrib import admin
from .models import Chauffeur

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'numero_piece', 'email', 'lieu_de_residence', 'nom_pere', 'nom_mere')
    search_fields = ('nom', 'prenom', 'numero_piece')
    list_filter = ('age', 'lieu_de_residence')
    ordering = ('nom', 'prenom')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Inclure des informations supplémentaires si nécessaire
        return qs

    def chauffeur_details(self, obj):
        # Exemple de méthode pour afficher des détails personnalisés
        return f"Email: {obj.email} | Téléphone: {obj.telephone}"

    chauffeur_details.short_description = 'Détails Chauffeur'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Ajoutez des informations supplémentaires à la page de détail
        extra_context = extra_context or {}
        chauffeur = self.get_object(request, object_id)
        extra_context['details'] = f"Chauffeur {chauffeur.nom} {chauffeur.prenom} : Email - {chauffeur.email}"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

