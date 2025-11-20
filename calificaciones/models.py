from django.db import models
from django.contrib.auth.models import User
from cursos.models import Materia

class Calificacion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Estudiante'})
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.username} - {self.materia.nombre}: {self.nota}"
