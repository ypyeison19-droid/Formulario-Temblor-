from django.shortcuts import render, redirect
from .models import RegistroTemblor

def inicio(request):
    return render(request, 'temblor/inicio.html')

def bienvenida(request):
    return render(request, 'temblor/bienvenida.html')

def crear_temblor(request):
    if request.method == 'POST':
        registro = RegistroTemblor.objects.create(
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
    registro = RegistroTemblor.objects.get(id=pk)
    return render(request, 'temblor/salida.html', {'registro': registro})