from django.contrib.auth.decorators import user_passes_test

def grupo_requiere(nombre_grupo):
    def en_grupo(user):
        return user.is_authenticated and (user.groups.filter(name=nombre_grupo).exists() or user.is_superuser)
    return user_passes_test(en_grupo)

profesor_requiere = grupo_requiere('Profesor')
admin_requiere = grupo_requiere('Admin')
estudiante_requiere = grupo_requiere('Estudiante')
