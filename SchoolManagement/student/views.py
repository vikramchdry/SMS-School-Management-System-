from django.shortcuts import render


# Create your views here.

def student_view(request):
    return render(request, 'student/student_base.html')


def student_click(request):
    return render(request, 'student/student_click.html')


def student_login(request):
    return render(request, 'student/student_login.html')


def student_dash(request):
    return render(request, 'student/student_dash.html')
