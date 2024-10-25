from django.shortcuts import render
from .models import Aviones
# Create your views here.
def listadoaviones(request):
    listadeaviones=Aviones.objects.all()
    return render(request, 'gestAviones.html',{"misaviones":listadeaviones})