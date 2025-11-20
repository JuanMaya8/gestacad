from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('asistencia/', views.listar_asistencia, name='listar_asistencia'),
    path('asistencia/crear/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencia/editar/<int:registro_id>/', views.editar_asistencia, name='editar_asistencia'),
    path('asistencia/eliminar/<int:registro_id>/', views.eliminar_asistencia, name='eliminar_asistencia'),

    path('asistencia/mi-asistencia/', views.asistencia_estudiante, name='asistencia_estudiante'),
]
