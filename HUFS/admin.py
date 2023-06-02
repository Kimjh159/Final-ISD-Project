from django.contrib import admin
from HUFS.models import Administrator, Class, Student, Timetable, MockTest, Visit, Teacher, Counseling, Room

admin.site.register(Administrator)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Timetable)
admin.site.register(MockTest)
admin.site.register(Visit)
admin.site.register(Teacher)
admin.site.register(Counseling)
admin.site.register(Room)

# Register your models here.
