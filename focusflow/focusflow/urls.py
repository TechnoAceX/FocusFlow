from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),   # ✅ NOT focusflow.core.urls
]