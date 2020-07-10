from django.shortcuts import render


# Create your views here.

def teacher_view(request):
    return render(request, 'teacher/teacher_base.html')


def teacher_click(request):
    return render(request, 'teacher/teacher_click.html')


def teacher_click(request):
    return render(request, 'teacher/teacher_login.html')


def teacher_signup(request):
    return render(request, 'teacher/teacher_signup.html')


def teacher_dash(request):
    return render(request, 'teacher/teacher_dash.html')
