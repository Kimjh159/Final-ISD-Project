from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def student(request):
    return render(request, 'student.html')


def timetable(request):
    return render(request, 'timetable.html')


def mocktestanalyze(request):
    return render(request, 'mocktestanalyze.html')


def teacher(request):
    return render(request, 'teacher.html')


def counseling(request):
    return render(request, 'counseling.html')


def visit(request):
    return render(request, 'visit.html')


def leave(request):
    return render(request, 'leave.html')
