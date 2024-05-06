from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .tasks import test_func #call the function to allocate it to celery
from activity.tasks import delete_all_activities
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

def test(request):
    test_func.delay()
    return HttpResponse("DONE")

def delete_all_activities_view(request):
    delete_all_activities.delay()
    return HttpResponse("All activities deleted")
