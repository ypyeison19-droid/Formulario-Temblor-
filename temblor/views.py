from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Alerta
from .serializers import RegistroTemblorSerializer

def inicio(request):
    return render(request, 'temblor/inicio.html')

def bienvenida(request):
    return render(request, 'temblor/bienvenida.html')

def crear_temblor(request):
    if request.method == 'POST':
        registro = Alerta.objects.create(
            nombre=request.POST.get('nombre'),
            magnitud=request.POST.get('magnitud'),
            profundidad=request.POST.get('profundidad'),
            rango=request.POST.get('rango'),
            lugar=request.POST.get('lugar'),
            area=request.POST.get('area'),
            fecha=request.POST.get('fecha'),
            hora=request.POST.get('hora')
        )
        return redirect('salida', pk=registro.id)
    return render(request, 'temblor/formulario.html')

def salida_temblor(request, pk):
    registro = Alerta.objects.get(id=pk)
    return render(request, 'temblor/salida.html', {'registro': registro})

# API ViewSet para React
class RegistroTemblorViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = RegistroTemblorSerializer