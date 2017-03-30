from django import forms
from .models import Persona
# from .models import Encuesta
# from django.db import models

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
        model= Persona
        fields ='__all__'

    def clean_email(self):
       cedula = self.cleaned_data.get("cedula")
       return cedula

# class EncuestaForm(forms.ModelForm):
#     class Meta:
#         model = Encuesta
#         fields = '__all__'
#
#
#     SIONO = (
#         ('S', 'SI'),
#         ('N', 'NO'),
#     )
#     SIONO2 = (
#         ('S', 'SI'),
#         ('N', 'NO'),
#         ('NOSE', 'NS'),
#     )
#     HACER = (
#         ('R', 'REGULARMENTE'),
#         ('A', 'A veces'),
#         ('NU', 'NUNCA'),
#     )
#     # cedula = models.ForeignKey(Registrado, null=True)
#
#     registrado = models.OneToOneField(
#         Registrado, null=False, blank=True,
#         on_delete=models.CASCADE,
#         primary_key=True
#     )
#     AEM = forms.MultipleChoiceField(choices=SIONO, widget=forms.CheckboxSelectMultiple)
#     lohace = forms.MultipleChoiceField(choices=SIONO, widget=forms.CheckboxSelectMultiple)
#     p2 = forms.MultipleChoiceField(choices=SIONO2, widget=forms.CheckboxSelectMultiple)
#     p3 = forms.MultipleChoiceField(choices=SIONO2,  widget=forms.CheckboxSelectMultiple)
#     p4 = forms.MultipleChoiceField(choices=SIONO2,  widget=forms.CheckboxSelectMultiple)
#     p5 = forms.MultipleChoiceField(choices=SIONO2,  widget=forms.CheckboxSelectMultiple)
#     p6 = forms.MultipleChoiceField(choices=SIONO2,  widget=forms.CheckboxSelectMultiple)
#     p7 = forms.MultipleChoiceField(choices=SIONO2, widget=forms.CheckboxSelectMultiple)
#
#
#     def __unicode__(self):
#         return str(self.registrado)
