from wtforms import Form
from wtforms import StringField,IntegerField,PasswordField,RadioField
from wtforms import EmailField
from wtforms import validators
from flask_wtf import FlaskForm

class UserForm(Form):
    matricula=IntegerField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=2,max=100,message='Ingresa valor valido')
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingrese nombre valido')
    ])
    apaterno=StringField('Apaterno',[
        validators.DataRequired(message='El campo es requerido')
    ])
    amaterno=StringField('Amaterno',[
        validators.DataRequired(message='El campo es requerido')
    ])
    email=EmailField('Correo',[
        validators.Email(message='Ingrese un correo valido')
    ])

class CinepolisForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    compradores = IntegerField('Cantidad de Compradores', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor válido")
    ])
    cineco = RadioField('Tarjeta Cineco', 
                       choices=[('no', 'No'), ('si', 'Si')],
                       default='no')
    boletos = IntegerField('Cantidad de Boletos', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor válido")
    ])