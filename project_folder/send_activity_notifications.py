from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from activity.models import Activity

class Command(BaseCommand):
    help = 'Check and send notifications for activities'

    def handle(self, *args, **options):
        current_time = datetime.now()
        target_time = current_time + timedelta(minutes=10)

        activities = Activity.objects.filter(start_time__gte=current_time, start_time__lte=target_time)

        for activity in activities:
            subject = 'Activity Notification'
            message = f"It's time for your activity: {activity.title}"
            from_email = 'your-email@gmail.com'
            recipient_list = ['receiver-email@example.com']

            send_mail(subject, message, from_email, recipient_list)

            print(f"Notification email sent for activity: {activity.title}")