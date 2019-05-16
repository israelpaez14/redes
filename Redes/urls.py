from django.conf.urls import url
from django.contrib import admin

from RedesProyecto.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_usuario),
    url(r'^abrir_salon/', abrir),
    url(r'^luces/', luces),
    url(r'^apagar_luces/', apagar_luces),
    url(r'^cerrar/', cerrar),
    url(r'^consultar/', preguntar_estado),
    url(r'^datos/', get_datos),
    url(r'^logout_view/', logout_view),
    url(r'^get_salas/', get_salas),
]
