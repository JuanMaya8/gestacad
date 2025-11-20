from django import forms
from .models import RegistroAsistencia

class RegistroAsistenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = ['estudiante', 'curso', 'fecha', 'presente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
