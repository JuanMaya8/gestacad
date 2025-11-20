from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    grupos = ['Admin', 'Profesor', 'Estudiante']
    for nombre in grupos:
        Group.objects.get_or_create(name=nombre)
