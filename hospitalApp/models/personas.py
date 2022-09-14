from django.db import models
from .logins import User

class Persona(models.Model):
    id_persona = models.CharField(primary_key=True,max_length= 20,unique=True,null=False,blank=False)
    login_id = models.OneToOneField(User,related_name='login_id', on_delete=models.CASCADE)
    nombres = models.CharField('NOMBRES',max_length= 100,null=False,blank=False)
    apellidos = models.CharField('APELLIDOS',max_length= 100,null=False,blank=False)
    genero = models.CharField('GENERO',max_length= 50)
    telefono = models.CharField('TELEFONO',max_length= 20,null=False,blank=False)
    