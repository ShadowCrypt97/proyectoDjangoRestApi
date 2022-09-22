from django.db import models

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True,unique=True,null=False,blank=False)
    nombre = models.CharField('nombre',max_length= 40,null=False,blank=False)
    descripcion = models.CharField('especialidad',max_length= 40,null=False,blank=False)