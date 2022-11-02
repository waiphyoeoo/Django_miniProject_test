from django.apps import AppConfig


class SeprateappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seprateApp'
    
    def ready(self):
        import seprateApp.signals