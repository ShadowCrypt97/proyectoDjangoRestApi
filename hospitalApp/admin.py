from django.contrib import admin
from .models.persona import User
from .models.rol import Rol
from .models.medico import Medico

# Register your models here.

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Medico)