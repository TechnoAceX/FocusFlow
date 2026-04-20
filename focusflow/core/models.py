from django.db import models
from django.contrib.auth.models import User

class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)  # ✅ dynamic
    hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)