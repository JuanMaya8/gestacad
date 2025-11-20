from django.db.models.signals import post_save
from django.dispatch import receiver
from trabajos.models import EntregaTrabajo
from calificaciones.models import Calificacion

@receiver(post_save, sender=EntregaTrabajo)
def actualizar_o_crear_calificacion(sender, instance, **kwargs):
    if instance.calificacion is not None:
        cal, created = Calificacion.objects.get_or_create(
            estudiante=instance.estudiante,
            materia=instance.trabajo.materia,
            defaults={'nota': instance.calificacion}
        )
        # Solo actualiza si la nota es distinta para evitar loops
        if not created and cal.nota != instance.calificacion:
            Calificacion.objects.filter(pk=cal.pk).update(nota=instance.calificacion)
