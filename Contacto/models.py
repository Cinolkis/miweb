from pyexpat import model
from django.db import models

# Create your models here.

class contacto(models.Model):
    nombre= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    contenido= models.CharField(max_length=200)

    class Meta:
        verbose_name="contacto"
        verbose_name_plural="contactos"

    def __str__(self):
        return self.nombre
