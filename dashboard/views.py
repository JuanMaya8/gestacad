from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from calificaciones.models import Calificacion
from asistencia.models import RegistroAsistencia
from inscripciones.models import Inscripcion 

@login_required
def dashboard(request):
    user = request.user
    grupos = user.groups.values_list('name', flat=True)
    context = {}

    if 'Admin' in grupos or user.is_superuser:
        context['rol'] = 'admin'
        context['total_usuarios'] = user.__class__.objects.count()
        context['total_cursos'] = Curso.objects.count()
        context['total_estudiantes'] = user.__class__.objects.filter(groups__name='Estudiante').count()

    elif 'Profesor' in grupos:
        context['rol'] = 'profesor'
        # Cursos donde el usuario es profesor de alguna materia
        context['cursos'] = Curso.objects.filter(profesor=user)

    elif 'Estudiante' in grupos:
        context['rol'] = 'estudiante'
        calificaciones = Calificacion.objects.filter(estudiante=user)
        context['calificaciones'] = calificaciones
        context['asistencias'] = RegistroAsistencia.objects.filter(estudiante=user)
        # Cursos inscritos usando la app inscripciones
        inscripciones = Inscripcion.objects.filter(estudiante=user).select_related('curso')
        context['cursos'] = [i.curso for i in inscripciones]

    else:
        context['rol'] = 'anonimo'

    return render(request, 'dashboard/dashboard.html', context)
