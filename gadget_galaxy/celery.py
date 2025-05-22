import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gadget_galaxy.settings')

app = Celery('gadget_galaxy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
