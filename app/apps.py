from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals
