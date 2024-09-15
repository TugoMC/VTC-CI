# vehicules/views.py
from django.shortcuts import render, get_object_or_404
from .models import Vehicule

def vehicule_details_view(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)
    return render(request, 'admin/vehicule_details.html', {'vehicule': vehicule})
