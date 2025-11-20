from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from usuarios.decorators import profesor_requiere, admin_requiere, estudiante_requiere
from .models import RegistroAsistencia
from .forms import RegistroAsistenciaForm
from django.db.models import Q

# Profesores y admins pueden listar y gestionar asistencias
@profesor_requiere
def listar_asistencia(request):
    registros = RegistroAsistencia.objects.select_related('estudiante', 'curso').all()
    return render(request, 'asistencia/listar_asistencia.html', {'asistencias': registros})

@profesor_requiere
def crear_asistencia(request):
    if request.method == 'POST':
        form = RegistroAsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:listar_asistencia')
    else:
        form = RegistroAsistenciaForm()
    return render(request, 'asistencia/crear_asistencia.html', {'form': form})

@profesor_requiere
def editar_asistencia(request, registro_id):
    registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
    if request.method == 'POST':
        form = RegistroAsistenciaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('asistencia:listar_asistencia')
    else:
        form = RegistroAsistenciaForm(instance=registro)
    return render(request, 'asistencia/editar_asistencia.html', {'form': form})

@profesor_requiere
def eliminar_asistencia(request, registro_id):
    registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
    if request.method == 'POST':
        registro.delete()
        return redirect('asistencia:listar_asistencia')
    return render(request, 'asistencia/eliminar_asistencia.html', {'registro': registro})

# Los estudiantes pueden ver solo su propia asistencia
@estudiante_requiere
@login_required
def asistencia_estudiante(request):
    asistencias = RegistroAsistencia.objects.filter(estudiante=request.user)
    return render(request, 'asistencia/asistencia_estudiante.html', {'asistencias': asistencias})   
