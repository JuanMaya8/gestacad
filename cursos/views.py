from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from usuarios.decorators import profesor_requiere, admin_requiere, grupo_requiere
from .models import Curso, Materia
from .forms import CursoForm, MateriaForm
from django.contrib import messages

# Control acceso para listar (todos los usuarios autenticados pueden ver)
@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

@login_required
def crear_curso(request):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser

    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para crear cursos.")
        return redirect('cursos:listar_cursos')

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.profesor = request.user  # <-- Asigna el profesor automáticamente
            curso.save()
            messages.success(request, "Curso creado y asignado a tu cargo.")
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

@login_required
def editar_curso(request, curso_id):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser
    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para editar cursos.")
        return redirect('cursos:listar_cursos')

    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso editado correctamente.")
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

@login_required
def eliminar_curso(request, curso_id):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser
    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para eliminar cursos.")
        return redirect('cursos:listar_cursos')

    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, "Curso eliminado correctamente.")
        return redirect('cursos:listar_cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})


@login_required
def listar_materias(request):
    materias = Materia.objects.select_related('curso').all()
    return render(request, 'cursos/listar_materias.html', {'materias': materias})

@login_required
def crear_materia(request):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser
    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para crear materias.")
        return redirect('cursos:listar_materias')

    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia creada correctamente.")
            return redirect('cursos:listar_materias')
    else:
        form = MateriaForm()
    return render(request, 'cursos/crear_materia.html', {'form': form})

@login_required
def editar_materia(request, materia_id):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser
    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para editar materias.")
        return redirect('cursos:listar_materias')

    materia = get_object_or_404(Materia, pk=materia_id)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia editada correctamente.")
            return redirect('cursos:listar_materias')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'cursos/editar_materia.html', {'form': form})

@login_required
def eliminar_materia(request, materia_id):
    es_profesor = request.user.groups.filter(name='Profesor').exists()
    es_admin = request.user.is_superuser
    if not (es_profesor or es_admin):
        messages.error(request, "No tienes permiso para eliminar materias.")
        return redirect('cursos:listar_materias')

    materia = get_object_or_404(Materia, pk=materia_id)
    if request.method == 'POST':
        materia.delete()
        messages.success(request, "Materia eliminada correctamente.")
        return redirect('cursos:listar_materias')
    return render(request, 'cursos/eliminar_materia.html', {'materia': materia})
