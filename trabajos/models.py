from django.db import models
from django.contrib.auth.models import User
from cursos.models import Materia

class Trabajo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='trabajos')
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Profesor'})
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_limite = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.materia.nombre})"

class EntregaTrabajo(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Estudiante'})
    archivo = models.FileField(upload_to='entregas/trabajos/')
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Entrega de {self.estudiante.username} para {self.trabajo.titulo}"
