from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trabajo, EntregaTrabajo
from cursos.models import Materia
from inscripciones.models import Inscripcion
from .forms import TrabajoForm, EntregaTrabajoForm, CalificarEntregaForm

def obtener_rol(user):
    grupos = user.groups.values_list('name', flat=True)
    if 'Profesor' in grupos or user.is_superuser:
        return 'profesor'
    elif 'Estudiante' in grupos:
        return 'estudiante'
    return None

@login_required
def listar_trabajos(request):
    rol = obtener_rol(request.user)
    if rol == 'profesor':
        trabajos = Trabajo.objects.filter(profesor=request.user).order_by('-fecha_creacion')
        return render(request, 'trabajos/listar_trabajos_profesor.html', {'trabajos': trabajos, 'rol': 'profesor'})
    elif rol == 'estudiante':
        inscritos = Inscripcion.objects.filter(estudiante=request.user).values_list('curso_id', flat=True)
        trabajos = Trabajo.objects.filter(materia__curso__id__in=inscritos).order_by('fecha_limite')
        return render(request, 'trabajos/listar_trabajos_estudiante.html', {'trabajos': trabajos, 'rol': 'estudiante'})
    else:
        messages.warning(request, "No tienes acceso a esta sección.")
        return redirect('dashboard:dashboard')

@login_required
def entregar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(Trabajo, id=trabajo_id)
    entrega, created = EntregaTrabajo.objects.get_or_create(trabajo=trabajo, estudiante=request.user)
    if request.method == 'POST':
        form = EntregaTrabajoForm(request.POST, request.FILES, instance=entrega)
        if form.is_valid():
            form.save()
            messages.success(request, "Trabajo entregado correctamente.")
            return redirect('trabajos:listar_trabajos')
    else:
        form = EntregaTrabajoForm(instance=entrega)
    return render(request, 'trabajos/entregar_trabajo.html', {'form': form, 'trabajo': trabajo})

@login_required
def crear_trabajo(request):
    rol = obtener_rol(request.user)
    if rol != 'profesor':
        messages.error(request, "Solo profesores pueden crear trabajos.")
        return redirect('trabajos:listar_trabajos')
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            trabajo = form.save(commit=False)
            trabajo.profesor = request.user
            trabajo.save()
            messages.success(request, "Trabajo creado con éxito.")
            return redirect('trabajos:listar_trabajos')
    else:
        form = TrabajoForm()
    return render(request, 'trabajos/crear_trabajo.html', {'form': form})

@login_required
def editar_trabajo(request, trabajo_id):
    rol = obtener_rol(request.user)
    trabajo = get_object_or_404(Trabajo, id=trabajo_id, profesor=request.user)
    if rol != 'profesor':
        messages.error(request, "Solo profesores pueden editar trabajos.")
        return redirect('trabajos:listar_trabajos')
    if request.method == 'POST':
        form = TrabajoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            messages.success(request, "Trabajo actualizado.")
            return redirect('trabajos:listar_trabajos')
    else:
        form = TrabajoForm(instance=trabajo)
    return render(request, 'trabajos/editar_trabajo.html', {'form': form})

@login_required
def eliminar_trabajo(request, trabajo_id):
    rol = obtener_rol(request.user)
    trabajo = get_object_or_404(Trabajo, id=trabajo_id, profesor=request.user)
    if rol != 'profesor':
        messages.error(request, "Solo profesores pueden eliminar trabajos.")
        return redirect('trabajos:listar_trabajos')
    if request.method == 'POST':
        trabajo.delete()
        messages.success(request, "Trabajo eliminado.")
        return redirect('trabajos:listar_trabajos')
    return render(request, 'trabajos/eliminar_trabajo.html', {'trabajo': trabajo})

@login_required
def revisar_entregas(request, trabajo_id):
    rol = obtener_rol(request.user)
    trabajo = get_object_or_404(Trabajo, id=trabajo_id, profesor=request.user)
    if rol != 'profesor':
        messages.error(request, "Solo profesores pueden revisar entregas.")
        return redirect('trabajos:listar_trabajos')
    entregas = EntregaTrabajo.objects.filter(trabajo=trabajo)
    return render(request, 'trabajos/revisar_entregas.html', {'trabajo': trabajo, 'entregas': entregas})

@login_required
def calificar_entrega(request, entrega_id):
    rol = obtener_rol(request.user)
    entrega = get_object_or_404(EntregaTrabajo, id=entrega_id, trabajo__profesor=request.user)
    if rol != 'profesor':
        messages.error(request, "Solo profesores pueden calificar entregas.")
        return redirect('trabajos:listar_trabajos')
    if request.method == 'POST':
        form = CalificarEntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrega calificada correctamente.")
            return redirect('trabajos:revisar_entregas', trabajo_id=entrega.trabajo.id)
    else:
        form = CalificarEntregaForm(instance=entrega)
    return render(request, 'trabajos/calificar_entrega.html', {'form': form, 'entrega': entrega})
