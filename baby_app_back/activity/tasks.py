
from activity.models import Activity
from celery import shared_task

@shared_task(bind=True)
def delete_all_activities(self):
    Activity.objects.all().delete()
    return "done"