from django.db import models

class Event(models.Model):
    host_name = models.CharField(max_length=100)
    event_name = models.CharField(max_length=200)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name

class Complaint(models.Model):
    roll_number = models.CharField(max_length=20)
    complaint_description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.roll_number} on {self.date_submitted}"
