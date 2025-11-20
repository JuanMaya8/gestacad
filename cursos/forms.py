from django import forms
from .models import Curso, Materia

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['curso', 'nombre', 'descripcion']
