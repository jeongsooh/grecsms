from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import index, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('evcharger/', include('evcharger.urls')),
    path('user/', include('user.urls')),
    path('charginginfo/', include('charginginfo.urls')),
    path('cardinfo/', include('cardinfo.urls')),
    path('ocpp16/', include('ocpp16.urls')),
    path('clients/', include('clients.urls')),
    path('variables/', include('variables.urls')),
    path('cpconfig/', include('cpconfig.urls')),
    path('msgapi/', include('msgapi.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('logout/', logout),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)