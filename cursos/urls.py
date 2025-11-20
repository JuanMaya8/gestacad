from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    # Cursos
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),

    # Materias
    path('materias/', views.listar_materias, name='listar_materias'),
    path('materias/crear/', views.crear_materia, name='crear_materia'),
    path('materias/editar/<int:materia_id>/', views.editar_materia, name='editar_materia'),
    path('materias/eliminar/<int:materia_id>/', views.eliminar_materia, name='eliminar_materia'),
]
    