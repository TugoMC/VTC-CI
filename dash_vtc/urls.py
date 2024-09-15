# dash_vtc/urls.py (ou urls.py de votre projet)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chauffeur/', include('chauffeur.urls')),
    path('vehicule/', include('vehicule.urls')),
    # autres URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
