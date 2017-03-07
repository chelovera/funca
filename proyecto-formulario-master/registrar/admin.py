from django.contrib import admin
from .models import Registrado
from .forms import RegistradoForm
# Register your models here.



class AdminRegistrado(admin.ModelAdmin):

    list_display = ["nombres","apellidos","cedula_de_identidad","sexo","direccion","ocupacion", "actualizado"]
    form = RegistradoForm
    class Meta:
         model = Registrado


admin.site.register(Registrado, AdminRegistrado)