from django.urls import path
from . import views

app_name = 'calificaciones'

urlpatterns = [
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:calificacion_id>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:calificacion_id>/', views.eliminar_calificacion, name='eliminar_calificacion'),

    # Nueva ruta para calificar entrega desde trabajos
    path('calificar-entrega/<int:entrega_id>/', views.calificar_entrega, name='calificar_entrega'),
    
    path('exportar/', views.exportar_calificaciones_csv, name='exportar_calificaciones'),

]
