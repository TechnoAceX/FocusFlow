from django.db import models

class StudySession(models.Model):
    subject = models.CharField(max_length=100)
    hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.hours}h"