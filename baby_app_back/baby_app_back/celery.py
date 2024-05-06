from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings

#celery beat 
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','baby_app_back.settings')
app = Celery('baby_app_back')
app.conf.enable_utc =False
app.conf.update(timezone = 'Africa/Algiers' )
app.config_from_object(settings,namespace = 'CELERY')

#CELERY BEAT SETTING 

app.conf.beat_schedule = {
    #add a task
    'delete_task_at_time' :{ # name 
        'task':'activity.tasks.delete_all_activities', # the app we created name . tasks . function name
        'schedule': crontab(hour=0,minute = 0 ),
    
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')
    
    #we can set a time or a period