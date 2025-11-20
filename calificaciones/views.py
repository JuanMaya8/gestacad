from django.shortcuts import render, get_object_or_404, redirect
import csv
from django.http import HttpResponse
from cursos.models import Curso, Materia
from django.contrib.auth.models import User
from .models import Calificacion
from .forms import CalificacionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from trabajos.models import EntregaTrabajo
from .utils import obtener_promedio_por_estudiante_curso, obtener_promedio_por_curso
import json

def es_profesor(user):
    return user.groups.filter(name='Profesor').exists() or user.is_superuser

def es_estudiante(user):
    return user.groups.filter(name='Estudiante').exists()

@login_required
def listar_calificaciones(request):
    user = request.user
    if es_profesor(user):
        cursos = Curso.objects.all()
        materias = Materia.objects.all()
        estudiantes = User.objects.filter(groups__name='Estudiante')

        curso_id = request.GET.get('curso') or None
        materia_id = request.GET.get('materia') or None
        estudiante_id = request.GET.get('estudiante') or None

        calificaciones = Calificacion.objects.select_related('estudiante', 'materia').all()
        if curso_id:
            calificaciones = calificaciones.filter(materia__curso_id=curso_id)
        if materia_id:
            calificaciones = calificaciones.filter(materia_id=materia_id)
        if estudiante_id:
            calificaciones = calificaciones.filter(estudiante_id=estudiante_id)

        promedios = obtener_promedio_por_estudiante_curso(calificaciones)
        promedios_json = json.dumps(promedios)
        return render(request, 'calificaciones/listar_calificaciones.html', {
            "calificaciones": calificaciones,
            "promedios": promedios,
            "promedios_json": promedios_json,
            "cursos": cursos,
            "materias": materias,
            "estudiantes": estudiantes,
            "filtro": {
                "curso": curso_id,
                "materia": materia_id,
                "estudiante": estudiante_id
            }
        })
    elif es_estudiante(user):
        calificaciones = Calificacion.objects.select_related('estudiante', 'materia').filter(estudiante=user)
        promedios = obtener_promedio_por_curso(calificaciones)
        
        # Convertir a JSON directamente - los valores ya son floats desde utils.py
        promedios_json = json.dumps({
            "labels": list(promedios.keys()),
            "data": list(promedios.values()),
        })
        
        return render(request, 'calificaciones/listar_calificaciones.html', {
            "calificaciones": calificaciones,
            "promedios": promedios,
            "promedios_json": promedios_json
        })
    else:
        return redirect('dashboard:dashboard')

@login_required
def crear_calificacion(request):
    user = request.user
    if not (user.groups.filter(name='Profesor').exists() or user.is_superuser):
        messages.error(request, "No tienes permiso para registrar calificaciones.")
        return redirect('calificaciones:listar_calificaciones')

    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Calificación guardada correctamente.")
            return redirect('calificaciones:listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear_calificacion.html', {'form': form})

@user_passes_test(es_profesor)
def editar_calificacion(request, calificacion_id):
    calificacion = get_object_or_404(Calificacion, pk=calificacion_id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar_calificacion.html', {'form': form})

@user_passes_test(es_profesor)
def eliminar_calificacion(request, calificacion_id):
    calificacion = get_object_or_404(Calificacion, pk=calificacion_id)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('calificaciones:listar_calificaciones')
    return render(request, 'calificaciones/eliminar_calificacion.html', {'calificacion': calificacion})

@login_required
@user_passes_test(es_profesor)
def calificar_entrega(request, entrega_id):
    entrega = get_object_or_404(EntregaTrabajo, id=entrega_id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.estudiante = entrega.estudiante
            calificacion.materia = entrega.trabajo.materia
            calificacion.save()
            entrega.calificacion = calificacion.nota
            entrega.save()
            messages.success(request, "Calificación guardada.")
            return redirect('trabajos:revisar_entregas', trabajo_id=entrega.trabajo.id)
    else:
        initial = {'nota': entrega.calificacion} if entrega.calificacion else {}
        form = CalificacionForm(initial=initial)
    return render(request, 'calificaciones/calificar_entrega.html', {'form': form, 'entrega': entrega})

@login_required
def exportar_calificaciones_csv(request):
    if not es_profesor(request.user):
        return redirect('calificaciones:listar_calificaciones')
    calificaciones = Calificacion.objects.select_related('estudiante', 'materia').all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="calificaciones.csv"'

    writer = csv.writer(response)
    writer.writerow(['Estudiante', 'Materia', 'Curso', 'Nota', 'Fecha'])
    for c in calificaciones:
        writer.writerow([
            c.estudiante.username,
            c.materia.nombre,
            c.materia.curso.nombre,
            c.nota,
            c.fecha_registro
        ])
    return response
