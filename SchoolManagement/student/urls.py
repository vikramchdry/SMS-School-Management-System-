from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.student_view,),
    path('student/', views.student_click, name = 'student'),
    path('login/', views.student_login , name = 'login'),
    path('dashboard/', views.student_dash, name = 'dashboard'),
]