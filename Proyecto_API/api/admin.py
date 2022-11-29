from django.contrib import admin
from .models import Aspirante, Cargo, EvaluacionAdmision, EstadoAdmision 
# Register your models here.
admin.site.register(Aspirante)
admin.site.register(Cargo)
admin.site.register(EvaluacionAdmision)
admin.site.register(EstadoAdmision)