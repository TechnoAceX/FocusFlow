from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # ✅ ADD THIS

urlpatterns = [
    path('', views.home, name='home'),
    path('add-session/', views.add_session, name='add_session'),
    path('reset-sessions/', views.reset_sessions, name='reset_sessions'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('subject-data/', views.subject_data, name='subject_data'),
]

