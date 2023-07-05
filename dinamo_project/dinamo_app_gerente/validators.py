import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import os

#Funcion para validar que el archivo subido sea un pdf
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('El archivo debe ser un pdf.')

#Funcion para validar que el archivo subido sea una imagen
def validate_file_extension_imgs(value):
    ext = os.path.splitext(value.name)[1] 
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('El archivo debe ser un pdf.')

#Funcion para validar que el campo solo contenga numeros
def validate_numeric(value):
    if not re.match('^[0-9]+$', value):
        raise ValidationError('Ingrese solo números.')


#Funcion para validar que el campo solo contenga letras y espacios
def validate_str(value):
    if not re.match('^[a-zA-Z ]+$', value):
        raise ValidationError('Ingrese solo letras.')

#Funcion para validar que el campo sea una fecha en formato dd-mm-aa
def validate_fecha_format(value):
    if not re.match(r'^\d{2}-\d{2}-\d{2}$', value):
        raise ValidationError('La fecha debe tener el formato dd-mm-aa y contener solo números.')
