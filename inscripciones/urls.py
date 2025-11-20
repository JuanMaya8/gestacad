from django.urls import path
from . import views

app_name = 'inscripciones'

urlpatterns = [
    path('cursos-disponibles/', views.cursos_disponibles, name='cursos_disponibles'),
    path('inscribir/<int:curso_id>/', views.inscribirse, name='inscribirse'),
    path('mis-cursos/', views.mis_cursos, name='mis_cursos'),
]
