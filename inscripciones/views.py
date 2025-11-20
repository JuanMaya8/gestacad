from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cursos.models import Curso
from .models import Inscripcion
from django.contrib import messages

@login_required
def cursos_disponibles(request):
    inscritos = Inscripcion.objects.filter(estudiante=request.user).values_list('curso_id', flat=True)
    cursos = Curso.objects.exclude(id__in=inscritos)
    return render(request, 'inscripciones/cursos_disponibles.html', {'cursos': cursos})

@login_required
def inscribirse(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if Inscripcion.objects.filter(estudiante=request.user, curso=curso).exists():
        messages.warning(request, "Ya estás inscrito en este curso.")
    else:
        Inscripcion.objects.create(estudiante=request.user, curso=curso)
        messages.success(request, f"Inscripción exitosa en {curso.nombre}.")
    return redirect('inscripciones:cursos_disponibles')

@login_required
def mis_cursos(request):
    inscripciones = Inscripcion.objects.filter(estudiante=request.user).select_related('curso')
    return render(request, 'inscripciones/mis_cursos.html', {'inscripciones': inscripciones})
