from django.db import models

from django.utils import timezone
from datetime import datetime , timedelta

class Activity(models.Model):
    TITLE_CHOICES = [
        ('sleep', 'Sleep'),
        ('medicine', 'Medicine'),
        ('eat', 'Eat'),
    ]
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    title = models.CharField(max_length=255, choices=TITLE_CHOICES)
    description = models.TextField()
    # days = MultiSelectField(choices=DAY_CHOICES, blank=True, max_length=100)  # Update the field to be blank
    days = models.CharField(max_length=255, choices=DAY_CHOICES)
    # Fields for 'eat' and sleep and medicine
    start_time = models.TimeField(blank=True, null=True)
    # Fields for 'sleep'

    sleep_end_time = models.TimeField(blank=True, null=True)

    # Fields for 'medicine'
    medicine_name = models.CharField(max_length=255, blank=True,null=True )

    medicine_expiration_date = models.DateField(blank=True, null=True)
    medicine_quantity = models.PositiveIntegerField(blank=True, null=True)
    medicine_instructions = models.TextField(blank=True, null=True , default='')


    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title == 'sleep':
            self.days = []  # Clear the days field for 'sleep' activity
            self.medicine_name = None
    
            self.medicine_expiration_date = None
            self.medicine_quantity = None
            self.medicine_instructions = None
            
        
    
        elif self.title == 'eat':
            self.days = []  # Clear the days field for 'eat' activity
    
            self.sleep_end_time = None
            self.medicine_name = None
    
            self.medicine_expiration_date = None
            self.medicine_quantity = None
            self.medicine_instructions = None
        super().save(*args, **kwargs)

    

    def is_today_matching_days(self):
        current_day = datetime.now().strftime("%A").lower()
        if current_day == self.days.lower() or current_day in self.days.lower().split(","):
            return True
        else:
            return False
        

    
    