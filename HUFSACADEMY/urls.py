from django.urls import path
from django.contrib import admin
from HUFS import views
from HUFS.views import CustomLoginView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('student/', views.student, name='student'),
    path('mocktestanalyze/', views.mocktestanalyze, name='mocktest_analyze'),
    path('teacher/', views.teacher, name='teacher'),
    path('timetable/', views.timetable, name='timetable'),
    path('counseling/', views.counseling, name='counseling'),
    path('visit/', views.visit, name='visit'),
    path('leave/', views.leave, name='leave'),
    path('mocktest_search/', views.mocktest_search, name='mocktest_search'),
    path('mocktest_search/recommend.html', views.recommend, name='recommend'),
]
