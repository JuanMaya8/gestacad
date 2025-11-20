from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            rol = form.cleaned_data['rol']
            try:
                grupo = Group.objects.get(name=rol)
                usuario.groups.add(grupo)
            except Group.DoesNotExist:
                return HttpResponseForbidden(f"Grupo '{rol}' no configurado.")
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    grupos = request.user.groups.all()
    return render(request, 'usuarios/perfil.html', {'usuario': request.user, 'grupos': grupos})
