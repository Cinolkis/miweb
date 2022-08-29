from django.shortcuts import render

from Contacto.form import FormularioContacto

# Create your views here.

def contacto(request):

    formulario_contacto= FormularioContacto()

    return render(request, "Contacto/contacto.html", {"miForm": formulario_contacto})