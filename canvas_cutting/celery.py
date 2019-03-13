from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from django.apps import apps
from django.conf import settings
import django






# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canvas_cutting.settings')

app = Celery('canvas_cutting')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

django.setup()

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
