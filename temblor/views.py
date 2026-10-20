from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Alerta
from .serializers import RegistroTemblorSerializer

def inicio(request):
    return render(request, 'temblor/inicio.html')

def bienvenida(request):
    return render(request, 'temblor/bienvenida.html')

@api_view(['GET', 'POST'])
def crear_temblor(request):
    if request.method == 'GET':
        registros = Alerta.objects.all().order_by('-id')
        serializer = RegistroTemblorSerializer(registros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistroTemblorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def salida_temblor(request, pk):
    registro = Alerta.objects.get(id=pk)
    return render(request, 'temblor/salida.html', {'registro': registro})

# API ViewSet para React
class RegistroTemblorViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = RegistroTemblorSerializer