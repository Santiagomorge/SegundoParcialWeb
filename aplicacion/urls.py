from django.urls import path
from . import views

urlpatterns = [
    path('aplicacion/', views.ListarAspirantes ),
    path('registrar/', views.CrearAspirante),
    path('ver_aspirantes/', views.aspiranteBD)
]