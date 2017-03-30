from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

SIONO = (
        (True,'Si'),
        (False,'No'),
    )
SEXOS = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )

SIONO2 = (
        (True,'Si'),
        (False,'No'),
        (None, 'No se'),

    )
HACER = (
        ('R', 'REGULARMENTE'),
        ('A', 'A veces'),
        ('NU', 'NUNCA'),
    )
CANCER = (
    ('CAM', 'Ca de Mama'),
    ('CAO', 'Ca de Ovario'),
    ('Otro', 'Otro Ca'),
)
ATEC = (
    ('T','Toracica'),
    ('G', 'Ginecol'),
    ('O', 'Otro'),
)
DENSI = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )
BIRAD =(
        ('0', 'Estudio insuficiente - Se recomienda'),
        ('1', 'Normal'),
        ('2', 'Anormal,Benigno'),
        ('3', 'Anormal, probablemente benigno'),
        ('4a', 'Anormal, probablemente benigno (baja)'),
        ('4b', 'Anormal, probablemente benigno(intermedia) '),
        ('4c', 'Anormal, probablemente benigno(alta)'),
        ('5', 'Anormal, maligno'),
        ('6', 'Anorma, maligno ya biopsiado'),
)

class Persona(models.Model):


    #encuesta = models.ForeignKey(Encuesta, null=True)
    cedula = models.IntegerField(blank=True, null=True, unique=True)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    paterno = models.CharField('Apellido Paterno',max_length=20, blank=False, null=False)
    materno = models.CharField('Apellido Materno',max_length=20, blank=True, null=True)
    del_marido = models.CharField('Apellido del Marido',max_length=20, blank=True, null=True)
    fecha_nac = models.DateField(blank=False, null=False)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null= True)
    direccion = models.CharField(max_length = 50, blank= True, null=True)
    sexo = models.CharField(max_length=3, choices=SEXOS,null= False)
    # sexo = MultiSelectField(choices=SEXOS, null=True)
    ocupacion = models.CharField(max_length = 50, blank = True, null = True)
    actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    AEM = models.CharField(verbose_name='Sabes lo que es?',default=False,choices=SIONO, max_length=3)
    loHace = models.CharField(verbose_name='Lo haces?', choices=HACER, default='NU' , max_length=3)
    bulto_pecho = models.CharField(verbose_name='Alguna vez sentiste un bulto en el pecho?',null=False,choices=SIONO2, max_length=3)
    problema_mama = models.CharField(verbose_name='Alguna vez consultaste por un problema de la mama?',choices=SIONO,default=False, max_length=3)
    mama_detalle= models.CharField(max_length= 200, blank=True, null= True)
    hizo_mamo = models.CharField(verbose_name='Alguna vez te hiciste Mamografia?',default=False,choices=SIONO, max_length=3)
    eco_mama= models.CharField(verbose_name='Alguna vez te hiciste una ecografia mamaria?',default=False,choices=SIONO, max_length=3)
    cancer_mama = models.CharField(verbose_name='Alguien en la familia alguna vez tuvo cancer de mama?',default=False,choices=SIONO, max_length=3)
    tenido_cancer = models.CharField(verbose_name='Conoces a alguien que haya tenido cancer de mama?',default=False,choices=SIONO, max_length=3)

    # AEM = MultiSelectField('sabes lo que es?', choices=SIONO, null=True, )
    # p2 = MultiSelectField('Alguna vez sentiste un bulto en el pecho?',   choices=SIONO2, null=True)
    # p3 = MultiSelectField('Alguna vez consultaste por un problema de la mama?', choices=HACER, null=True)
    # p4 = MultiSelectField('Alguna vez te hiciste Mamografia', choices=SIONO, null=True)
    # p5 = MultiSelectField('Alguna vez te hiciste Ecografia Mamaria?', choices=SIONO, null=True)
    # p6 = MultiSelectField('Alguien la familia alguna vez tuvo cancer de mama?', choices=SIONO, null=True)
    # p7 = MultiSelectField('Conoces a alguien que haya tenido cancer de mama?', choices=SIONO, null=True)

    def __unicode__(self):
        return str(self.cedula)

    def __str__(self):
        return str (self.nombres)+ " " +str(self.paterno)

    class Meta:
        verbose_name = 'Ficha de Paciente'
        verbose_name_plural = 'Ficha de Pacientes'

class Mamografia(models.Model):
    class Meta:
        verbose_name = 'Mamografia'
        verbose_name_plural = 'Mamografias'

    registrado = models.OneToOneField(
        Persona, null=False, blank=True,
        on_delete=models.CASCADE,
        primary_key=True
    )
    mamoDespi = models.CharField('Mamografia despistaje',max_length=100, null=True, blank=True)
    mamoDiag = models.CharField('Mamografia Diagnostica',max_length=100, null=True, blank=True)
    nodulo = models.CharField('Nodulo', max_length=100, null=True, blank=True)
    antecedentes = models.CharField('Antecedentes familiares', max_length=100, null=True, blank=True)
    otros = models.CharField('Otros factores de riesgo',max_length=100, null=True, blank=True)
    densidad = models.CharField('Densidad', choices=DENSI, null=True, max_length=3)
    descripcion=models.CharField('Descripcion', max_length=100, null=True)
    birads = models.CharField('BIRADS', choices = BIRAD, null= True, max_length=3)
    eg = models.CharField('EG', max_length=100, null=True)
    hallazgos = models.CharField('Hallazgos?, si o no y descripcion', max_length=100, null=True)
    des_birads = models.CharField('Birads', max_length=150, null=True)

    def __unicode__(self):
        return str(self.registrado)


class Antecedentes (models.Model):

    class Meta:
        verbose_name = 'Ficha de Recoleccion de Dato'
        verbose_name_plural = 'Ficha de Recoleccion de Datos'

    cirugia_mamaria = models.CharField('Cirugias Mamarias', max_length=3, null= True, choices=SIONO)
    otras_cirugias = models.CharField('Otras Cirugias', max_length=3, null=True, choices=SIONO)
    antecedentes = models.CharField('Antecedentes de Cancer', max_length=3, choices=CANCER)
    ante_fam = models.CharField('Hay antecedentes familiares?', max_length=3, choices=SIONO)
    cancer_mama = models.CharField('Cancer de mama', max_length=3, choices=SIONO)
    cancer_ovario = models.CharField('Cancer de ovario', max_length=3, choices=SIONO)
    cancer_prostata = models.CharField('Cancer de prostata', max_length=3, choices=SIONO)
    cancer_colon = models.CharField('Cancer de colon', max_length=3, choices=SIONO)
    cancer_otro = models.CharField('Otro cancer', max_length=3, choices=SIONO, )
    hijos = models.CharField(max_length=3, choices=SIONO)
    numero = models.IntegerField()
    edad_primero = models.IntegerField('Edad del Primero?', blank=True, null=True)
    amamanto = models.CharField('Amamanto?', max_length=3, choices=SIONO, blank=True, null=True)
    tiempo = models.IntegerField(blank=True, null=True)
