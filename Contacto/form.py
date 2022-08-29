from email.message import EmailMessage
from tkinter.tix import Form
from django import forms

class FormularioContacto(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=100, required=True)

    email= forms.CharField(label="Email", max_length=50, required=True)

    contenido= forms.CharField(label="Contenido", widget=forms.Textarea)