#from os import PRIO_USER
from django.shortcuts import render, redirect

from Contacto.form import FormularioContacto
from django.core.mail import EmailMessage

from Contacto.models import contacto

# Create your views here.

def contacto(request):
    formulario_contacto= FormularioContacto()

    if request.method=="POST":
        formulario_contacto= FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST["nombre"]
            email=request.POST["email"]
            contenido=request.POST["contenido"]

            correo= EmailMessage("Django"," El user con name {} con el email {} escribe lo siguiente {}".format(nombre, email, contenido),"",["cinolkis87@gmail.com"],reply_to=[email])
            try:
                correo.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "Contacto/contacto.html", {"miForm": formulario_contacto})