from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    ROL_CHOICES = (
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
    )
    rol = forms.ChoiceField(choices=ROL_CHOICES, required=True, label='¿Eres estudiante o profesor?')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rol']
