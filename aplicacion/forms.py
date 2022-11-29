from django import forms

class CrearNuevoAspirante(forms.Form):
    tipoDocumento = forms.CharField(label="tipoDocumento", max_length=200)
    numeroDocumento = forms.CharField(label="numeroDocumento", max_length=200)
    nombre = forms.CharField(label="nombre", max_length=200)
    apellido = forms.CharField(label="apellido", max_length=200)
    profesion = forms.CharField(label="profesion", max_length=200)
    edad = forms.IntegerField(label="edad")
    ciudad = forms.CharField(label="ciudad", max_length=200)