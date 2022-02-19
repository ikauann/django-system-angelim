from django.apps import AppConfig


class BlingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bling'

    def ready(self):
        from task.Scheduler import start_scheduler
        start_scheduler()