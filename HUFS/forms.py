from django import forms
from HUFS.models import Student, Timetable, MockTest, Teacher, Counseling, Visit


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        error_messages = {
            'stu_birth': {
                'invalid': '올바른 날짜 형식을 입력해주세요 (YYYY-MM-DD).',},
            'stu_leave_date': {
                'invalid': '올바른 날짜 형식을 입력해주세요 (YYYY-MM-DD).',},
        }


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'

class MockTestForm(forms.ModelForm):
    class Meta:
        model = MockTest
        fields = '__all__'
        error_messages = {
            'date': {
                'invalid': '올바른 날짜 형식을 입력해주세요 (YYYY-MM).', },

        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class CounselingForm(forms.ModelForm):
    class Meta:
        model = Counseling
        fields = '__all__'
        error_messages = {
            'cou_date': {
                'invalid': '올바른 날짜 형식을 입력해주세요 (YYYY-MM-DD).', },
        }

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        error_messages = {
            'visit_date': {
                'invalid': '올바른 날짜 형식을 입력해주세요 (YYYY-MM-DD).', },
        }
