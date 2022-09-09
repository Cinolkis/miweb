from email.message import EmailMessage
from tkinter.tix import Form
from django import forms

class FormularioContacto(forms.Form):
    nombre= forms.CharField(label="Nombre", required=True)

    email= forms.CharField(label="Email", required=True)

    contenido= forms.CharField(label="Contenido", widget=forms.Textarea)