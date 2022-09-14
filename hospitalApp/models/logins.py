from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def createUser(self, username, password=None):
        """
        Crear y guardar un usuario con el nombre y contraseña dados.
        """
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario.')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def createSuperUser(self,username,password):
        """
        Crear y guardar un super usuario con el nombre y contraseña dados.
        """
        user = self.createUser(
            username=username,
            password=password
        )
        
        user.is_admin = True
        user.save(using = self._db)
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True,auto_created=True,null=False,blank=False,unique=True)
    username = models.CharField('username',max_length= 20,unique=True)
    password = models.CharField('password',max_length=256)
    
    def save(self,**kwargs):
        someSalt = 'mMUj0DrIK6vgtdIYepkIxN',
        self.password = make_password(self.password,someSalt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'
        