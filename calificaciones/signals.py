from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Calificacion
from trabajos.models import EntregaTrabajo

@receiver(post_save, sender=Calificacion)
def sync_entrega_trabajo(sender, instance, **kwargs):
    entregas = EntregaTrabajo.objects.filter(
        estudiante=instance.estudiante,
        trabajo__materia=instance.materia
    )
    for entrega in entregas:
        # Solo actualiza si la nota es distinta
        if entrega.calificacion != instance.nota:
            EntregaTrabajo.objects.filter(pk=entrega.pk).update(calificacion=instance.nota)
            # Opcional: agrega para ver sincronización en logs de desarrollo
            # print(f'Nota sincronizada: entrega {entrega.id} materia {instance.materia} estudiante {instance.estudiante}')
