from django.urls import path
from .views import Aspirante, crear_aspirante
from . import views

#app_name = 'api'
urlpatterns=[
    path('aspirante/', views.Aspirante),
    path('crear_aspirante/', views.crear_aspirante),
]