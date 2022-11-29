from django.db import models

# Create your models here.

class Aspirante(models.Model):
    tipoDocumento = models.CharField('tipoDocumento', max_length=200)
    numeroDocumento = models.CharField('numeroDocumento', max_length=200)
    nombre = models.CharField('nombre', max_length=200)
    apellido = models.CharField('apellido', max_length=200)
    profesion = models.CharField('profesion', max_length=200)
    edad = models.IntegerField('edad', max_length=200)
    ciudad = models.CharField('ciudad', max_length=200)

class Cargo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField(max_length=200)

class EvaluacionAdmision(models.Model):
    fecha = models.DateField(max_length=200)
    puntosHojaVida = models.IntegerField(max_length=200)
    puntosExperiencia = models.IntegerField(max_length=200)
    puntosPostgrados = models.IntegerField(max_length=200)
    puntosCertificaciones = models.IntegerField(max_length=200)
    puntosIngles = models.IntegerField(max_length=200)
    totalPuntos = models.IntegerField(max_length=200)

class EstadoAdmision(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField(max_length=200)
