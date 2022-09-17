from rest_framework import serializers
from hospitalApp.models.logins import User
from hospitalApp.models.medicos import Medico
from hospitalApp.models.personas import Persona
from hospitalApp.serializers.medicoSerializer import MedicoSerializer
from hospitalApp.serializers.personaSerializer import PersonaSerializer


class UserMedicoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()
    medico = MedicoSerializer()
    class Meta:
        model = User
        fields = ['id','username','password','persona','medico']
    
    def create(self,validated_data):
        personaData = validated_data.pop('persona')
        medicoData = validated_data.pop('medico')
        userInstance = User.objects.create(**validated_data)
        personaInstance = Persona.objects.create(login_id=userInstance, **personaData)
        Medico.objects.create(persona_id = personaInstance, **medicoData)
        return userInstance                    
    
    def to_representation(self,obj):
        user = User.objects.get(id = obj.id)
        persona = Persona.objects.get(login_id = obj.id)
        medico = Medico.objects.get(persona_id = persona.id_persona)
        return {
            'id': user.id,
            'username': user.username,
            'persona':{
                'id_persona': persona.id_persona,
                'nombres': persona.nombres,
                'apellidos': persona.apellidos,
                'genero': persona.genero,
                'telefono': persona.telefono
            },
            'medico':{
                'id_medico': medico.id_medico,
                'especialidad': medico.especialidad,
                'fecha_registro': medico.fecha_registro
            }
        }            