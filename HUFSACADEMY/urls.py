from django.urls import path
from django.contrib import admin
from HUFS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('mocktestanalyze/', views.mocktestanalyze, name='mocktest_analyze'),
    path('teacher/', views.teacher, name='teacher'),
    path('timetable/', views.timetable, name='timetable'),
    path('counseling/', views.counseling, name='counseling'),
    path('visit/', views.visit, name='visit'),
    path('leave/', views.leave, name='leave'),
]
