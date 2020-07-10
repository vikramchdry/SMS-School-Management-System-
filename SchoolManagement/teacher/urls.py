from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher_view, name = "teacher"),
    path('teacherclick/', views.teacher_click, name = "teacherclick"),
    path('teacherlogin/', views.teacher_click, name = "teacherlogin"),
    path('teachersignup/', views.teacher_signup, name = "teachersignup"),
    path('tdashboard/', views.teacher_signup, name = "tdashboard"),
]