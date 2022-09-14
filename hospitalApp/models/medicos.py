from django.db import models
from .personas import Persona

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True,unique=True,null=False,blank=False)
    persona_id = models.ForeignKey(Persona,related_name='PERSONA_ID', on_delete=models.CASCADE)
    especialidad = models.CharField('ESPECIALIDAD',max_length= 40,null=False,blank=False)
    fecha_registro = models.DateField('FECHA_REGISTRO',null=False,blank=False)
