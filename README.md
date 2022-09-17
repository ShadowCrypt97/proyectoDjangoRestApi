# Creación de environment virtual:
* python -m venv env

# Ejecución environment Script:
* env\Scripts\activate

# instalación de django dentro del entorno:
* pip install django
* pip install djangorestframework

# instalación de librería simpleJWT:
* pip install djangorestframework-simplejwt

# instalación driver de postgresql:
* pip install psycopg2

# Creación de proyecto
* django-admin startproject projectName .
### Nota: donde dice projectName lo cambiamos por el nombre de nuestro proyecto

# Modificando el settings.py
* Nos dirigimos a la carpeta del proyecto en VSC y añadimos al final en el arreglo que se llama INSTALLED_APPS la llave 'rest_framework'
* ## añadimos la siguiente configuración del rest framework:
~~~
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
~~~
* ## Creamos la siguiente variable SimpleJWT para configurar la autenticación por JWT:
~~~
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
} 
~~~
* ### nota: para mayor información sobre simpleJWT ver la documentación:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html.

* ## Añadimos la configuración de la base de datos:
~~~
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '5432',
    }
}
~~~
# Creación de aplicación
* django-admin startapp hospitalApp

# Ejecutamos la aplicación
* python manage.py runserver

# Comandos para realizar la migración
* python manage.py makemigrations hospitalApp
* python manage.py migrate 

# Despliegue en Heroku:
* Se debe crear un archivo llamado requirements.txt
* Se debe hacer el comando <<pip3 freeze>> para obtener las dependencias del proyecto
* Se copian las dependencias en el archivo requirements.txt
* Se añaden las siguientes 2 dependencias que nos permitiran el despliegue a Heroku:
    1. gunicorn==20.1.0
    2. django-heroku==0.3.1