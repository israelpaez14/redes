from datetime import date, datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from RedesProyecto.models import Salon, Horario


def get_salas(request):
    salas = Salon.objects.all()

    lista =[]

    for sala in salas:
        lista.append({"nombre":sala.nombre})

    return JsonResponse({"data":lista}, safe=False)



@csrf_exempt
def login_usuario(request):
    usuario = request.POST.get("usuario")
    password = request.POST.get("password")
    print(usuario)
    print(password)

    if usuario is None or password is None:
        return HttpResponse("Bad request", status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=usuario, password=password)
    print(user)
    if user is None:
        return HttpResponse("Usuario o password incorrectos", status=status.HTTP_403_FORBIDDEN)

    login(request, user)
    print(user.email)

    return HttpResponse("Sesion iniciada", status=status.HTTP_200_OK)


@csrf_exempt
def abrir(request):
    usuario_actual = request.user


    print(usuario_actual)
    salon = request.POST.get("salon")
    print(salon)

    salon_obj = Salon.objects.get(nombre=salon)

    ahora = datetime.now()

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    h = Horario.objects.filter(salon=salon_obj, dia=dias[ahora.date().weekday()], usuario=usuario_actual,
                               hora_inicio__lte=ahora.time().hour, hora_final__gt=ahora.time().hour)

    if h.first() is None:
        return HttpResponse("No es su horario", status=status.HTTP_403_FORBIDDEN)

    salon_obj.estado = True

    salon_obj.save()
    return HttpResponse("Salon abierto", status=status.HTTP_200_OK)


@csrf_exempt
def luces(request):
    usuario_actual = request.user
    salon = request.POST.get("salon")

    salon_obj = Salon.objects.get(nombre=salon)

    ahora = datetime.now()

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    h = Horario.objects.filter(salon=salon_obj, dia=dias[ahora.date().weekday()], usuario=usuario_actual,
                               hora_inicio__lte=ahora.time().hour, hora_final__gt=ahora.time().hour)

    if h.first() is None:
        return HttpResponse("No es su horario",  status=status.HTTP_403_FORBIDDEN)

    salon_obj.luces = True

    salon_obj.save()
    return HttpResponse("Luces encendidas", status=status.HTTP_200_OK)


@csrf_exempt
def apagar_luces(request):
    usuario_actual = request.user
    salon = request.POST.get("salon")

    salon_obj = Salon.objects.get(nombre=salon)

    ahora = datetime.now()

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    h = Horario.objects.filter(salon=salon_obj, dia=dias[ahora.date().weekday()], usuario=usuario_actual,
                               hora_inicio__lte=ahora.time().hour, hora_final__gt=ahora.time().hour)

    if h.first() is None:
        return HttpResponse("No es su horario",  status=status.HTTP_403_FORBIDDEN)

    salon_obj.luces = False

    salon_obj.save()
    return HttpResponse("Luces Apagadas", status=status.HTTP_200_OK)


@csrf_exempt
def cerrar(request):
    usuario_actual = request.user
    salon = request.POST.get("salon")

    salon_obj = Salon.objects.get(nombre=salon)

    ahora = datetime.now()

    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

    h = Horario.objects.filter(salon=salon_obj, dia=dias[ahora.date().weekday()], usuario=usuario_actual,
                               hora_inicio__lte=ahora.time().hour, hora_final__gt=ahora.time().hour)

    if h.first() is None:
        return HttpResponse("No es su horario",  status=status.HTTP_403_FORBIDDEN)

    salon_obj.estado = False

    salon_obj.save()
    return HttpResponse("Salon cerrado", status=status.HTTP_200_OK)


def preguntar_estado(request):
    salon = request.GET.get("salon")
    print(salon)
    salon_obj = Salon.objects.get(nombre=salon)

    usuario = None
    diferencia = 0

    if salon_obj.estado:
        ahora = datetime.now()

        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

        h = Horario.objects.filter(salon=salon_obj, dia=dias[ahora.date().weekday()],
                                   hora_inicio__lte=ahora.time().hour, hora_final__gt=ahora.time().hour).first()

        if h is not None:
            usuario = h.usuario

            hora_salon = datetime.strptime(
                str(ahora.month) + "/" + str(ahora.day) + "/" + str(ahora.year) + " " + str(h.hora_final) + ":00:00",
                '%m/%d/%Y %H:%M:%S')
            print(hora_salon)
            print(ahora)
            diferencia = (hora_salon - ahora).seconds / 60

            print(diferencia)

            if diferencia <= 5:
                salon_obj.estado = False
                salon_obj.luces = False
                salon_obj.save()

    return JsonResponse({"estado": salon_obj.estado, "usuario": usuario.username if usuario is not None else None,
                         "restante": int(diferencia),
                         "luces": salon_obj.luces}, safe=False)


def get_datos(request):
    usuario = request.user

    return JsonResponse({"nombre": usuario.first_name, "apellido": usuario.last_name, "email": usuario.email},
                        safe=False)


def logout_view(request):
    logout(request)
    return HttpResponse("Sesion cerrada", status=status.HTTP_200_OK)
