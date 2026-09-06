from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router para la API REST
router = DefaultRouter()
router.register(r'temblores', views.RegistroTemblorViewSet)

urlpatterns = [
    # Rutas HTML anteriores
    path('', views.inicio, name='inicio'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('temblor/', views.crear_temblor, name='formulario'),
    path('temblor/salida/<int:pk>/', views.salida_temblor, name='salida'),

    # Incluir las rutas de la API bajo el prefijo api/
    path('api/', include(router.urls)),
]