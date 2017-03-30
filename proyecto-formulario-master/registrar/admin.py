from django.contrib import admin
# from multiselectfield.admin import msf_filter
# from multiselectfield.admin import MSFChoiceListFilter
from .models import Persona, Mamografia

# from .forms import RegistradoForm
# from .forms import EncuestaForm
# Register your models here.

# class EncuestaAdmin(admin.ModelAdmin):
#     # model = Encuesta
#     # list_display = ['registrado']
#     # list_filter = (
#     #       ('p1', MSFChoiceListFilter),
#     # )
#
#     fieldsets = (
#          ('AEM AUTOEXAMEN MAMARIO', {
#              'fields': ('AEM', 'loHace', 'p2', 'p3', 'p4', 'p5', 'p6'),
#          }),
#     )
#      # extra = 5
#      # class Meta:
#      #     model = Encuesta
#
#
class AdminRegistrado(admin.ModelAdmin):
    #inlines = [encuestaInLine]
    list_display = ["nombres","paterno", "materno", "del_marido","cedula","sexo","direccion","ocupacion", "actualizado"]

    # form = RegistradoForm
    list_filter = ['cedula',]
    ordering = ['cedula',]


    fieldsets = (
        ('IDENTIFICACION',{

            'fields': ( ('paterno', 'materno', 'del_marido'), 'nombres', ('sexo', 'fecha_nac'), ('cedula', 'ocupacion'))
        }),
        ('DIRECCION', {
            'fields': ( 'direccion', ('telefono', 'celular'))
        }),
        ('AEM AUTOEXAMEN MAMARIO', {
                      'fields': ('AEM', 'loHace','bulto_pecho',('problema_mama', 'mama_detalle'),'hizo_mamo','eco_mama','cancer_mama','tenido_cancer'),
                   }),
        # ('ENCUESTA', {
        #     # 'classes': ('collapse','in'),
        #     'fields': ('encuesta',),
        # }),
    )
    radio_fields = {'sexo':admin.VERTICAL,'AEM':admin.VERTICAL,'loHace':admin.HORIZONTAL,'bulto_pecho':admin.HORIZONTAL,'problema_mama':admin.VERTICAL,
                    'hizo_mamo':admin.VERTICAL,'eco_mama':admin.VERTICAL,'cancer_mama':admin.VERTICAL, 'tenido_cancer':admin.VERTICAL}
# class AdminMamo(admin.ModelAdmin):
#     list_display = ["registrado.nombres", "registrado.cedula"]

class AdminMamo(admin.ModelAdmin):
    list_display = ["mamoDespi","mamoDiag","nodulo","antecedentes", "otros","densidad","descripcion", "birads", "eg",
    "hallazgos", "des_birads"]
    radio_fields = {'densidad': admin.HORIZONTAL, 'birads': admin.VERTICAL}

admin.site.register(Persona, AdminRegistrado)
# admin.site.register(Encuesta)
admin.site.register(Mamografia,AdminMamo)
admin.site.site_header = "FUNCA"
admin.site.site_title = "Administracion del sitio"
