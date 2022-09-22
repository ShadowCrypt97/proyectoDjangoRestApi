from rest_framework import serializers
from hospitalApp.models import persona
from hospitalApp.models.persona import User
from hospitalApp.models.medico import Medico

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ['id_persona','nombres','apellidos','genero','telefono','username','password','email','rol','medico']
    
    def create(self,validated_data):
        rolData = validated_data.pop('rol')
        medicoData = validated_data.pop('medico')
        personaInstance = User.objects.create(**validated_data)
        rolInstance = User.objects.create(rol_id=personaInstance, **rolData)
        Medico.objects.create(persona_id = personaInstance, **medicoData)
        return personaInstance                    
    
    def to_representation(self,obj):
        persona = User.objects.get(id = obj.id)
        rol = User.objects.get(rol_id = obj.id)
        medico = Medico.objects.get(persona_id = persona.id_persona)
        return {
            'id_persona': persona.id_persona,
            'username': persona.username,
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'genero': persona.genero,
            'telefono': persona.telefono,
            'email': persona.email,
            'rol':{
                'id': rol.id,
                'nombre': rol.nombre,
                'descripcion':rol.descripcion              
            },
            'medico':{
                'id_medico': medico.id_medico,
                'especialidad': medico.especialidad,
                'fecha_registro': medico.fecha_registro
            }
        }