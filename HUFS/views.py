# Create your views here.
from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Max

from HUFS.models import MockTest, Student


def home(request):
    return render(request, 'home.html')


def student(request):
    return render(request, 'student.html')


def timetable(request):
    return render(request, 'timetable.html')


def mocktest_search(request):
    student_number = request.GET.get('student_number')
    date = request.GET.get('date')

    stud = Student.objects.get(stu_num=student_number)
    class_type = stud.class_class_type.class_type

    selectedstu = MockTest.objects.filter(student_stu_num=stud, date=date)
    selectedmock = MockTest.objects.filter(student_stu_num=stud, date=date)

    selectedmock_values = []
    difference = []

    for mocktest in selectedmock:
        mocktest_values = {
            'mock_id': mocktest.mock_id,
            'mock_kor': mocktest.mock_kor,
            'mock_math': mocktest.mock_math,
            'mock_eng': mocktest.mock_eng,
            'mock_extraclass_1': mocktest.mock_extraclass_1,
            'mock_extraclass_2': mocktest.mock_extraclass_2,
            'date': mocktest.date,
            'student_stu_num': mocktest.student_stu_num,
        }
        selectedmock_values.append(mocktest_values)
        avg_class_mocktests = MockTest.objects.filter(student_stu_num__class_class_type__class_type=class_type,
                                                      date=date).aggregate(
            mock_kor__avg=Avg('mock_kor'),
            mock_math__avg=Avg('mock_math'),
            mock_eng__avg=Avg('mock_eng'),
            mock_extraclass_1__avg=Avg('mock_extraclass_1'),
            mock_extraclass_2__avg=Avg('mock_extraclass_2')
        )

        avg_same_curri_mocktests = MockTest.objects.filter(
            student_stu_num__stu_curriculum=stud.stu_curriculum,
            date=date
        ).aggregate(
            mock_kor__avg=Avg('mock_kor'),
            mock_math__avg=Avg('mock_math'),
            mock_eng__avg=Avg('mock_eng'),
            mock_extraclass_1__avg=Avg('mock_extraclass_1'),
            mock_extraclass_2__avg=Avg('mock_extraclass_2'),
        )

        # Calculate the difference for each field
        diff = {}
        for field in ['mock_kor', 'mock_math', 'mock_eng', 'mock_extraclass_1', 'mock_extraclass_2']:
            selectedmock_value = getattr(mocktest, field)
            avg_mocktest_value = avg_class_mocktests[field + '__avg']
            diff[field] = selectedmock_value - avg_mocktest_value
        difference.append(diff)

    context = {
        'student_data_list': selectedstu,
        'selectedmock_values': selectedmock_values,
        'difference': difference,
        'mocktests': [avg_class_mocktests],
        'avg_same_curri_mocktests': [avg_same_curri_mocktests],

    }

    return render(request, 'mocktestanalyze.html', context)


def mocktestanalyze(request):
    max_student_number = Student.objects.aggregate(Max('stu_num'))['stu_num__max']
    student_number = request.GET.get('student_stu_num')
    date = request.GET.get('date')

    queryset = MockTest.objects.filter(student_stu_num=student_number, date=date)

    context = {
        'student_data_list': queryset
    }
    return render(request, 'mocktestanalyze.html', context)



def recommend(request):
    student_number = request.GET.get('student_number')
    date = request.GET.get('date')

    stud = Student.objects.get(stu_num=student_number)
    class_type = stud.class_class_type.class_type
    selectedname=stud[0]

    selectedstu = MockTest.objects.filter(student_stu_num=stud, date=date)
    selectedmock = MockTest.objects.filter(student_stu_num=stud, date=date)

    selectedmock_values = []
    difference = []

    for mocktest in selectedmock:
        mocktest_values = {
            'mock_id': mocktest.mock_id,
            'mock_kor': mocktest.mock_kor,
            'mock_math': mocktest.mock_math,
            'mock_eng': mocktest.mock_eng,
            'mock_extraclass_1': mocktest.mock_extraclass_1,
            'mock_extraclass_2': mocktest.mock_extraclass_2,
            'date': mocktest.date,
            'student_stu_num': mocktest.student_stu_num,
        }
        selectedmock_values.append(mocktest_values)
        avg_class_mocktests = MockTest.objects.filter(student_stu_num__class_class_type__class_type=class_type,
                                                      date=date).aggregate(
            mock_kor__avg=Avg('mock_kor'),
            mock_math__avg=Avg('mock_math'),
            mock_eng__avg=Avg('mock_eng'),
            mock_extraclass_1__avg=Avg('mock_extraclass_1'),
            mock_extraclass_2__avg=Avg('mock_extraclass_2')
        )
        diff = {}
        for field in ['mock_kor', 'mock_math', 'mock_eng', 'mock_extraclass_1', 'mock_extraclass_2']:
            selectedmock_value = getattr(mocktest, field)
            avg_mocktest_value = avg_class_mocktests[field + '__avg']
            diff[field] = selectedmock_value - avg_mocktest_value
        difference.append(diff)

    context = {
        'student_data_list': selectedstu,
        'selectedmock_values': selectedmock_values,
        'difference': difference,
        'name':selectedname
    }

    return render(request, 'recommend.html', context)


def teacher(request):
    return render(request, 'teacher.html')


def counseling(request):
    return render(request, 'counseling.html')


def visit(request):
    return render(request, 'visit.html')


def leave(request):
    return render(request, 'leave.html')
