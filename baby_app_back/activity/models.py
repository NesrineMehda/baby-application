from django.db import models

class Activity(models.Model):
    TITLE_CHOICES = (
        ('sleep', 'Sleep'),
        ('medicine', 'Medicine'),
        ('eat', 'Eat'),
    )
    
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    description = models.TextField()
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title