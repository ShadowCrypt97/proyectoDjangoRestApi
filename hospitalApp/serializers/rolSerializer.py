from rest_framework import serializers
from hospitalApp.models.rol import Rol



class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre','descripcion']
    