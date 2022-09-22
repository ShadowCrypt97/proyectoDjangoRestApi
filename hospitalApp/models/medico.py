from django.db import models
from .persona import User

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True,unique=True,null=False,blank=False)
    persona_id = models.ForeignKey(User,related_name='persona_id', on_delete=models.CASCADE)
    especialidad = models.CharField('ESPECIALIDAD',max_length= 40,null=False,blank=False)
    fecha_registro = models.DateField('FECHA_REGISTRO',null=False,blank=False)
