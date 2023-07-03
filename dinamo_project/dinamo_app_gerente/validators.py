import re
from django.core.exceptions import ValidationError
import os

#Funcion para validar que el archivo subido sea un pdf
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('El archivo debe ser un pdf.')

#Funcion para validar que el campo cedula (en el modelo Usuraio) solo contenga numeros
def validate_numeric(value):
    if not re.match('^[0-9]+$', value):
        raise ValidationError('Ingrese solo números.')
    