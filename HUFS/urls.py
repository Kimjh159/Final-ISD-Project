from django.urls import path
from HUFS import views

urlpatterns = [
    path('', views.student, name='student'),

    path('', views.timetable, name='timetable'),

    path('', views.mocktest, name='mocktest'),

    path('', views.mocktestanalyze, name='mocktestanalysis'),

    path('', views.teacher, name='teacher'),

    path('', views.counseling, name='counseling'),

    path('', views.visit, name='visit'),



]
