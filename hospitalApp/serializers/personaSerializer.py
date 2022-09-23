from rest_framework import serializers
from hospitalApp.models.persona import User
from hospitalApp.models.medico import Medico
from hospitalApp.models.rol import Rol
from hospitalApp.serializers.medicoSerializer import MedicoSerializer
from hospitalApp.serializers.rolSerializer import RolSerializer

class PersonaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer()
    class Meta:
        model = User
        fields = ['id','nombres','apellidos','genero','telefono','username','password','email','medico']
    
    def create(self,validated_data):
        medicoData = validated_data.pop('medico')
        rol = Rol.objects.get(id_rol= 1)
        personaInstance = User.objects.create(rol_id= rol,**validated_data)
        Medico.objects.create(persona_id = personaInstance, **medicoData)
        return personaInstance                    
    
    def to_representation(self,obj):
        persona = User.objects.get(id = obj.id)
        rol = Rol.objects.get(id_rol= persona.rol_id.id_rol)
        medico = Medico.objects.get(persona_id = persona.id)
        return {
            'id_persona': persona.id,
            'username': persona.username,
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'genero': persona.genero,
            'telefono': persona.telefono,
            'email': persona.email,
            'rol':{
                'id': rol.id_rol,
                'nombre': rol.nombre,
                'descripcion':rol.descripcion              
            },
            'medico':{
                'id': medico.id_medico,
                'especialidad': medico.especialidad,
                'fecha_registro': medico.fecha_registro
            }
        }