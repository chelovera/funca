from django import forms
from .models import Registrado

# class formPaciente(forms.Form):
#
#     cedula_de_identidad = forms.IntegerField()
#     nombre_form = forms.CharField(max_length=100)
#     apellidos = forms.CharField(max_length=100)
#     fecha_nac = forms.DateField()
#     telefono = forms.IntegerField()
#     #actualizado = forms.DateTimeField()


class RegistradoForm(forms.ModelForm):
    class Meta:
        model= Registrado
        fields = ["cedula_de_identidad","nombres", "apellidos","fecha_nac","sexo","direccion","ocupacion","telefono", "celular", ]

    def clean_email(self):
       cedula = self.cleaned_data.get("cedula_de_identidad")
       return cedula