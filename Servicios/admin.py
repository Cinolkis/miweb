from pyexpat import model
from django.contrib import admin

from Servicios.models import Servicios
from Servicios.models import Servicios 

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicios, ServiciosAdmin)
