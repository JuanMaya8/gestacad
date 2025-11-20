from django import forms
from .models import Trabajo, EntregaTrabajo

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['materia', 'titulo', 'descripcion', 'fecha_limite']

class EntregaTrabajoForm(forms.ModelForm):
    class Meta:
        model = EntregaTrabajo
        fields = ['archivo']

class CalificarEntregaForm(forms.ModelForm):
    class Meta:
        model = EntregaTrabajo
        fields = ['calificacion', 'observaciones']
