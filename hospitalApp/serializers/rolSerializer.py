from rest_framework import serializers
from hospitalApp.models.rol import Rol



class UserMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol','nombre','descripcion']
    