from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
import json

from .models import StudySession


# 🔥 ADD SESSION (API)
@login_required
def add_session(request):
    if request.method == "POST":
        data = json.loads(request.body)

        StudySession.objects.create(
            user=request.user,
            subject=data['subject'],                 # dynamic subject
            hours=data['duration'] / 60             # store in hours
        )

        return JsonResponse({"status": "success"})


# 🔥 RESET SESSIONS
@login_required
def reset_sessions(request):
    if request.method == "POST":
        StudySession.objects.filter(user=request.user).delete()
        return JsonResponse({"status": "cleared"})


# 🔥 SIGNUP
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # password check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        # create user
        User.objects.create_user(
            username=username,
            password=password1,
            email=email
        )

        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, 'signup.html')


# 🔥 HOME DASHBOARD
@login_required
def home(request):
    sessions = StudySession.objects.filter(user=request.user)

    last_7_days = []
    sessions_per_day = []

    for i in range(6, -1, -1):
        day = timezone.now().date() - timedelta(days=i)

        day_sessions = sessions.filter(created_at__date=day)

        total_minutes = sum(s.hours * 60 for s in day_sessions)
        count_sessions = day_sessions.count()

        last_7_days.append(int(total_minutes))
        sessions_per_day.append(count_sessions)

    context = {
        "study_minutes_json": json.dumps(last_7_days),
        "sessions_per_day_json": json.dumps(sessions_per_day),
    }

    return render(request, "home.html", context)


# 🔥 SUBJECT GRAPH DATA (DYNAMIC)
@login_required
def subject_data(request):
    data = (
        StudySession.objects
        .filter(user=request.user)
        .values('subject')
        .annotate(total_hours=Sum('hours'))
        .order_by('-total_hours')   # optional: sort by highest
    )

    # convert hours → minutes for UI
    formatted = [
        {
            "subject": d["subject"],
            "total_minutes": int(d["total_hours"] * 60)
        }
        for d in data
    ]

    return JsonResponse(formatted, safe=False)