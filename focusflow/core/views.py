from django.http import JsonResponse
import json
from .models import StudySession

def add_session(request):
    if request.method == "POST":
        data = json.loads(request.body)

        StudySession.objects.create(
            user=request.user,
            subject=data['subject'],
            hours=data['duration'] / 60
        )

        return JsonResponse({"status": "success"})
    
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.http import JsonResponse
from .models import StudySession

def reset_sessions(request):
    if request.method == "POST":
        StudySession.objects.all().delete()
        return JsonResponse({"status": "cleared"})