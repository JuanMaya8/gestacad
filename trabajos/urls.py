from django.urls import path
from . import views

app_name = 'trabajos'

urlpatterns = [
    # Vista única que muestra lista según rol (profesor o estudiante)
    path('trabajos/', views.listar_trabajos, name='listar_trabajos'),

    # Entregar trabajo (solo estudiante)
    path('entregar-trabajo/<int:trabajo_id>/', views.entregar_trabajo, name='entregar_trabajo'),

    # Acciones de profesor
    path('profesor/trabajos/crear/', views.crear_trabajo, name='crear_trabajo'),
    path('profesor/trabajos/editar/<int:trabajo_id>/', views.editar_trabajo, name='editar_trabajo'),
    path('profesor/trabajos/eliminar/<int:trabajo_id>/', views.eliminar_trabajo, name='eliminar_trabajo'),
    path('profesor/trabajos/<int:trabajo_id>/entregas/', views.revisar_entregas, name='revisar_entregas'),
    path('profesor/entrega/<int:entrega_id>/calificar/', views.calificar_entrega, name='calificar_entrega'),
]
