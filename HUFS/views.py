# Create your views here.
from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Max
from HUFS.models import MockTest, Student, recommendclass
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import TemplateView
import requests

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def get_current_weather():
    api_key = '2622e56dd1fb9c00db5b24599a7b7d4e'
    city = 'Seoul'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'weather' in data:
        current_weather = data['weather'][0]['main']
        current_temperature = int(data['main']['temp'] - 273.15)
    else:
        current_weather = '날씨 정보를 가져오지 못했습니다'
        current_temperature = None
    return current_weather, current_temperature

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        current_weather, current_temperature = get_current_weather()  # 외부 날씨 API를 사용하여 현재 날씨 정보 가져오기
        context['current_date'] = current_date
        context['current_weather'] = current_weather
        context['current_temperature'] = current_temperature
        return context




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
    selectedname = stud.stu_name

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
        'name': selectedname,

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


from decimal import Decimal


def recommend(request):
    student_number = request.GET.get('student_number')
    date = request.GET.get('date')

    stud = Student.objects.get(stu_num=student_number)
    class_type = stud.class_class_type.class_type
    selectedname = stud.stu_name

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
        signs = {}

        for field in ['mock_kor', 'mock_math', 'mock_eng', 'mock_extraclass_1', 'mock_extraclass_2']:
            selectedmock_value = getattr(mocktest, field)
            avg_mocktest_value = avg_class_mocktests[field + '__avg']
            difference_value = selectedmock_value - avg_mocktest_value

            if difference_value > 2:
                signs[field] = 'positive'
            else:
                signs[field] = 'negative'

            diff[field] = difference_value

        difference.append(diff)

    rec_info = recommendclass.objects.filter(rec_classtype__contains=class_type)
    rec_kor = rec_info.filter(rec_class='MOCK_KOR')
    rec_math = rec_info.filter(rec_class='MOCK_MATH')
    rec_eng = rec_info.filter(rec_class='MOCK_ENG')
    rec_ex = rec_info.filter(rec_class='MOCK_EXTRACLASS')

    rec_kor_pro = rec_kor.values_list('rec_pro', flat=True)
    rec_kor_cost = rec_kor.values_list('rec_price', flat=True)
    rec_kor_weight = rec_kor.values_list('rec_weightpl', flat=True)[0] if signs[
                                                                              'mock_kor'] == 'positive' else \
    rec_kor.values_list(
        'rec_weightmi', flat=True)[0]
    rec_kor_weight = float(rec_kor_weight)
    rec_kor_adj = 0 if selectedmock_values[0]['mock_kor'] >= 92 else 2
    rec_kor_totalprice = (rec_kor_cost[0] * rec_kor_weight * abs(diff['mock_kor'] * rec_kor_adj)) // 10000 * 10000

    rec_math_pro = rec_math.values_list('rec_pro', flat=True)
    rec_math_cost = rec_math.values_list('rec_price', flat=True)
    rec_math_weight = rec_math.values_list('rec_weightpl', flat=True)[0] if signs[
                                                                                'mock_math'] == 'positive' else \
    rec_math.values_list(
        'rec_weightmi', flat=True)[0]
    rec_math_weight = float(rec_math_weight)
    rec_math_adj = 0 if selectedmock_values[0]['mock_math'] >= 92 else 2
    rec_math_totalprice = (rec_math_cost[0] * rec_math_weight * abs(diff['mock_math']) * rec_math_adj) // 10000 * 10000

    rec_eng_pro = rec_eng.values_list('rec_pro', flat=True)
    rec_eng_cost = rec_eng.values_list('rec_price', flat=True)
    rec_eng_weight = rec_eng.values_list('rec_weightpl', flat=True)[0] if signs[
                                                                              'mock_eng'] == 'positive' else \
    rec_eng.values_list(
        'rec_weightmi', flat=True)[0]
    rec_eng_weight = float(rec_eng_weight)
    rec_eng_adj = 0 if selectedmock_values[0]['mock_eng'] >= 90 else 2
    rec_eng_totalprice = (rec_eng_cost[0] * rec_eng_weight * abs(diff['mock_eng']) * rec_eng_adj) // 10000 * 10000

    rec_ex_pro = rec_ex.values_list('rec_pro', flat=True)
    rec_ex_cost = rec_ex.values_list('rec_price', flat=True)
    rec_ex_weight = rec_ex.values_list('rec_weightpl', flat=True)[0] if signs[
                                                                            'mock_extraclass_1'] == 'positive' else \
    rec_ex.values_list(
        'rec_weightmi', flat=True)[0]
    rec_ex_weight = float(rec_ex_weight)
    rec_eng_adj = 0 if (selectedmock_values[0]['mock_extraclass_1'] + selectedmock_values[0][
        'mock_extraclass_2']) / 2 >= 90 else 2
    rec_ex_totalprice = (rec_ex_cost[0] * rec_ex_weight * abs(diff['mock_extraclass_1'])*rec_eng_adj) // 10000 * 10000

    rec_totalprice = rec_kor_totalprice+rec_math_totalprice+rec_eng_totalprice+rec_ex_totalprice
    context = {
        'student_data_list': selectedstu,
        'selectedmock_values': selectedmock_values,
        'difference': difference,
        'name': selectedname,
        'rec_kor_pro': rec_kor_pro,
        'rec_kor_totalprice': rec_kor_totalprice,
        'rec_math_pro': rec_math_pro,
        'rec_math_totalprice': rec_math_totalprice,
        'rec_eng_pro': rec_eng_pro,
        'rec_eng_totalprice': rec_eng_totalprice,
        'rec_ex_pro': rec_ex_pro,
        'rec_ex_totalprice': rec_ex_totalprice,
        'rec_totalprice': rec_totalprice,

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
