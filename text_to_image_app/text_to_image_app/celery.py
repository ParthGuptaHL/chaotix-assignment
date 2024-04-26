from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#celery configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_to_image_app.settings')

app = Celery('text_to_image_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()