from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Estudiante'})
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante.username} inscrito en {self.curso.nombre}"
