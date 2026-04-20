from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import StudySession

@login_required
def subject_data(request):
    data = (
        StudySession.objects
        .filter(user=request.user)
        .values('subject')
        .annotate(total_hours=Sum('hours'))
    )
    
    return JsonResponse(list(data), safe=False)