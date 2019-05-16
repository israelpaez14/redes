from django.contrib import admin
from django.urls import path
from RedesProyecto.views import login_usuario, abrir, luces, cerrar, preguntar_estado, apagar_luces, get_datos, \
    logout_view, get_salas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_usuario),
    path('abrir_salon/', abrir),
    path('luces/', luces),
    path('apagar_luces/', apagar_luces),
    path('cerrar/', cerrar),
    path('consultar/', preguntar_estado),
    path('datos/', get_datos),
    path('logout_view/', logout_view),
    path('get_salas/', get_salas),
]
