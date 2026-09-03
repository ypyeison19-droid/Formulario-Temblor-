from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('temblor/', views.crear_temblor, name='formulario'),
    path('temblor/salida/<int:pk>/', views.salida_temblor, name='salida'),
]