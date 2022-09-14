from django.contrib import admin
from .models.logins import User
from .models.personas import Persona
from .models.medicos import Medico

# Register your models here.

admin.site.register(User)
admin.site.register(Persona)
admin.site.register(Medico)