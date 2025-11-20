from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos_a_cargo', null=True, blank=True)  # <-- CAMBIO: profesor a cargo

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='materias')

    def __str__(self):
        return f"{self.nombre} ({self.curso.nombre})"
