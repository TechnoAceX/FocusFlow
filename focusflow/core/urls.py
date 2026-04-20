
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-session/', views.add_session, name='add_session'),  # ✅ ADD THIS
]

path('reset-sessions/', views.reset_sessions),

