from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso

class RegistroAsistencia(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Estudiante'})
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ('estudiante', 'curso', 'fecha')

    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.estudiante.username} - {self.curso.nombre} - {self.fecha}: {estado}"
