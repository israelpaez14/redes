from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Salon(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    estado = models.BooleanField(default=False)
    luces = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    hora_inicio = models.IntegerField()
    hora_final = models.IntegerField()
    dia = models.CharField(max_length=255)
    salon = models.ForeignKey(Salon, null=False, blank=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.salon) + " " + str(self.hora_inicio) + "-" + str(self.hora_final)+"-"+str(self.dia)
