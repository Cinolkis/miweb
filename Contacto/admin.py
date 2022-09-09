from django.contrib import admin

# Register your models here.

from Contacto.models import contacto

class contactoAdmin(admin.ModelAdmin):
    list_display= ("nombre","email")
    search_fields=("nombre","email")

admin.site.register(contacto, contactoAdmin)