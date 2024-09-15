from django.shortcuts import get_object_or_404, render

from chauffeur.models import Chauffeur

def chauffeur_details_view(request, id):
    chauffeur = get_object_or_404(Chauffeur, id=id)
    return render(request, 'admin/chauffeur_details.html', {'chauffeur': chauffeur})
