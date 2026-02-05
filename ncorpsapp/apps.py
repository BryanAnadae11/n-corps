from django.apps import AppConfig


class NcorpsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ncorpsapp'

    def ready(self):
    	import ncorpsapp.signals
