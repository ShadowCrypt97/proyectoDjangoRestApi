# Creación de environment virtual:
* python -m venv env

# Ejecución environment Script:
* env\Scripts\activate

# instalación de django dentro del entorno:
* pip install django
* pip install djangorestframework

# Creación de proyecto
* django-admin startproject projectName
### Nota: donde dice projectName lo cambiamos por el nombre de nuestro proyecto

# Modificando el settings.py
* Nos dirigimos a la carpeta del proyecto en VSC y añadimos al final en el arreglo que se llama INSTALLED_APPS la llave 'rest_framework'

# Creación de aplicación
* django-admin startapp hospitalApp

# Ejecutamos la aplicación
* python manage.py runserver