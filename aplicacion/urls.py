from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('aplicacion/', views.ListarAspirantes ),
    path("listarPorCargo/", views.listarEvaluaciones),
    path('registrar/', views.CrearAspirante),
    path('ver_aspirantes/', views.aspiranteBD)
]