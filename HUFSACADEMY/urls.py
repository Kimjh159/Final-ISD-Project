from django.urls import path
from django.contrib import admin
from HUFS import views
from HUFS.views import CustomLoginView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),

    path('student/', views.student, name='student'),
    path('student/new/', views.create_student, name='add_student'),
    path('student/update/<int:stu_num>/', views.update_student, name = 'update_student'),
    path('student/delete/<int:stu_num>/', views.delete_student, name = 'delete_student'),

    path('mocktestanalyze/', views.mocktestanalyze, name='mocktest_analyze'),

    path('mocktest/', views.mocktest, name='mocktest'),
    path('mocktest/new/', views.create_mocktest, name='add_mocktest'),
    path('mocktest/update/<int:mock_id>/', views.update_mocktest, name = 'update_mocktest'),
    path('mocktest/delete/<int:mock_id>/', views.delete_mocktest, name = 'delete_mocktest'),

    path('teacher/', views.teacher, name='teacher'),
    path('teacher/new/', views.create_teacher, name='add_teacher'),
    path('teacher/update/<int:tea_num>/', views.update_teacher, name = 'update_teacher'),
    path('teacher/delete/<int:tea_num>/', views.delete_teacher, name = 'delete_teacher'),

    path('timetable/', views.timetable, name='timetable'),
    path('timetable/new/', views.create_timetable, name='add_timetable'),
    path('timetable/update/<int:tita_num>/', views.update_timetable, name = 'update_timetable'),
    path('timetable/delete/<int:tita_num>/', views.delete_timetable, name = 'delete_timetable'),


    path('counseling/', views.counseling, name='counseling'),
    path('counseling/new/', views.create_counseling, name='add_counseling'),
    path('counseling/update/<int:cou_num>/', views.update_counseling, name = 'update_counseling'),
    path('counseling/delete/<int:cou_num>/', views.delete_counseling, name = 'delete_counseling'),

    path('visit/', views.visit, name='visit'),
    path('visit/new/', views.create_visit, name='add_visit'),
    path('visit/update/<int:visit_num>/', views.update_visit, name = 'update_visit'),
    path('visit/delete/<int:visit_num>/', views.delete_visit, name = 'delete_visit'),

    path('mocktest_search/', views.mocktest_search, name='mocktest_search'),
    path('mocktest_search/recommend.html', views.recommend, name='recommend'),
]
