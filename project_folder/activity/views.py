from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ActivitySerializer
from .models import Activity
import threading
from datetime import datetime, time
from django.utils import timezone
import time
from django.core.mail import send_mail
from myaccount.models import User

@api_view(['GET'])
def getActivity(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createActivity(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



def is_midnight():
        current_time = timezone.now().time()
        midnight = datetime.combine(timezone.now().date(), datetime.min.time()).time()

        if current_time == midnight:
            return True
        else:
            return False
        
def delete_activities_if_midnight():
    if is_midnight():
        activities = Activity.objects.all()
        current_day = datetime.now().strftime("%A").lower()

        for activity in activities:
            if activity.is_today_matching_days():
                days_list = activity.days.lower().split(",")
                days_list = [day for day in days_list if day != current_day]

                activity.days = ",".join(days_list)
                activity.save()
            elif not activity.is_today_matching_days() and not activity.days:
                activity.delete()
'''
def run_scheduled_tasks():
    while True:
        delete_activities_if_midnight()
        time.sleep(60)  # Wait for 60 seconds before checking again

task_thread = threading.Thread(target=run_scheduled_tasks)
task_thread.start()
'''