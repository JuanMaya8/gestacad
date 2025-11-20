from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home/landing simple
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Apps con namespaces para uso correcto en templates
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('cursos/', include(('cursos.urls', 'cursos'), namespace='cursos')),
    path('calificaciones/', include(('calificaciones.urls', 'calificaciones'), namespace='calificaciones')),
    path('asistencia/', include(('asistencia.urls', 'asistencia'), namespace='asistencia')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),

    # Apps adicionales
    path('inscripciones/', include(('inscripciones.urls', 'inscripciones'), namespace='inscripciones')),
    path('trabajos/', include(('trabajos.urls', 'trabajos'), namespace='trabajos')),  # <--- Agregado trabajos
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)