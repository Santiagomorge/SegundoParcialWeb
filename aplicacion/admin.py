from django.contrib import admin
from .models import Aspirante, Cargo, EstadoAdmision, EvaluacionAdmision

# Register your models here.
admin.site.register(Aspirante)
admin.site.register(Cargo)
admin.site.register(EvaluacionAdmision)
admin.site.register(EstadoAdmision)