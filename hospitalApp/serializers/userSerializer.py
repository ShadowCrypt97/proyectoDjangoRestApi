from rest_framework import serializers
from hospitalApp.models.logins import User
from hospitalApp.models.personas import Persona
from hospitalApp.serializers.personaSerializer import PersonaSerializer


class UserSerializer(serializers.ModelSerializer):
    login_id = PersonaSerializer()
    class Meta:
        model = User
        fields = ['id','username','password','login_id']
    
    def create(self,validated_data):
        personaData = validated_data.pop('login_id')
        userInstance = User.objects.create(**validated_data)
        Persona.objects.create(login_id=userInstance, **personaData)
        return userInstance                    
    
    def to_representation(self,obj):
        user = User.objects.get(id = obj.id)
        persona = Persona.objects.get(login_id = obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'persona':{
                'id_persona': persona.id_persona,
                'nombres': persona.nombres,
                'apellidos': persona.apellidos,
                'genero': persona.genero,
                'telefono': persona.telefono
            }
        }            