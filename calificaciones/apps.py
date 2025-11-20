from django.apps import AppConfig

class CalificacionesConfig(AppConfig):
    name = 'calificaciones'

    def ready(self):
        import calificaciones.signals
