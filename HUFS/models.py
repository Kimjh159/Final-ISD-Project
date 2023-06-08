from django.db import models


class Administrator(models.Model):
    admin_num = models.PositiveIntegerField(db_column='ADMIN_NUM', primary_key=True)
    admin_name = models.CharField(db_column='ADMIN_NAME', max_length=4)
    admin_age = models.PositiveIntegerField(db_column='ADMIN_AGE')

    def __str__(self):
        return self.admin_name



    class Meta:
        managed = True
        db_table = 'administrator'


class Class(models.Model):
    class_type = models.CharField(db_column='CLASS_TYPE', primary_key=True, max_length=2)
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')

    def __str__(self):
        return self.class_type



    class Meta:
        managed = True
        db_table = 'class'


class Counseling(models.Model):
    cou_num = models.PositiveIntegerField(db_column='COU_NUM', primary_key=True)
    cou_date = models.DateField(db_column='COU_DATE')
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')
    student_stu_num = models.ForeignKey('Student', models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')

    def __str__(self):
        return f"{self.cou_date} {self.student_stu_num.stu_name}"

    class Meta:
        managed = True
        db_table = 'counseling'


class MockTest(models.Model):
    mock_id = models.PositiveIntegerField(db_column='MOCK_ID', primary_key=True)
    mock_kor = models.PositiveIntegerField(db_column='MOCK_KOR')
    mock_math = models.PositiveIntegerField(db_column='MOCK_MATH')
    mock_eng = models.PositiveIntegerField(db_column='MOCK_ENG')
    mock_extraclass_1 = models.PositiveIntegerField(db_column='MOCK_EXTRACLASS_1')
    mock_extraclass_2 = models.PositiveIntegerField(db_column='MOCK_EXTRACLASS_2')
    date = models.TextField()
    student_stu_num = models.ForeignKey('Student', models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')

    def __str__(self):
        return f"{self.student_stu_num}{self.date}"

    class Meta:
        managed = True
        db_table = 'mock_test'


class Room(models.Model):
    room_num = models.PositiveIntegerField(db_column='ROOM_NUM', primary_key=True)
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')

    def __str__(self):
        return f" {self.room_num}"

    class Meta:
        managed = True
        db_table = 'room'


class Student(models.Model):
    stu_num = models.PositiveIntegerField(db_column='STU_NUM', primary_key=True)
    stu_name = models.CharField(db_column='STU_NAME', max_length=4)
    stu_age = models.PositiveIntegerField(db_column='STU_AGE')
    stu_sex = models.CharField(db_column='STU_SEX', max_length=1)
    stu_birth = models.DateField(db_column='STU_BIRTH')
    stu_curriculum = models.CharField(db_column='STU_CURRICULUM', max_length=1)
    stu_extraclass_1 = models.CharField(db_column='STU_EXTRACLASS_1', max_length=2)
    stu_extraclass_2 = models.CharField(db_column='STU_EXTRACLASS_2', max_length=2)
    stu_formerexam = models.DecimalField(db_column='STU_FORMEREXAM', max_digits=3,
                                         decimal_places=2)
    stu_leave_date = models.DateField(db_column='STU_LEAVE_DATE')
    stu_leave_reason = models.CharField(db_column='STU_LEAVE_REASON', max_length=100)
    room_room_num = models.ForeignKey(Room, models.DO_NOTHING, db_column='ROOM_ROOM_NUM')
    class_class_type = models.ForeignKey(Class, models.DO_NOTHING,
                                         db_column='CLASS_CLASS_TYPE')

    def __str__(self):
        return f"{self.stu_num}"



    class Meta:
        managed = True
        db_table = 'student'


class Teacher(models.Model):
    tea_num = models.PositiveIntegerField(db_column='TEA_NUM', primary_key=True)
    tea_name = models.CharField(db_column='TEA_NAME', max_length=4)
    tea_age = models.PositiveIntegerField(db_column='TEA_AGE')
    tea_sex = models.CharField(db_column='TEA_SEX', max_length=1)
    tea_subject = models.CharField(db_column='TEA_SUBJECT', max_length=2)

    def __str__(self):
        return f"{self.tea_subject} {self.tea_name}"



    class Meta:
        managed = True
        db_table = 'teacher'


class Timetable(models.Model):
    tita_num = models.PositiveIntegerField(db_column='TITA_NUM', primary_key=True)
    tita_day = models.CharField(db_column='TITA_DAY', max_length=1)
    tita_1c = models.CharField(db_column='TITA_1C', max_length=2)
    tita_2c = models.CharField(db_column='TITA_2C', max_length=2)
    tita_3c = models.CharField(db_column='TITA_3C', max_length=2)
    tita_4c = models.CharField(db_column='TITA_4C', max_length=2)
    class_class_type = models.ForeignKey(Class, models.DO_NOTHING,
                                         db_column='CLASS_CLASS_TYPE')

    def __str__(self):
        return f"{self.tita_day} {self.class_class_type.class_type}"


    class Meta:
        managed = True
        db_table = 'timetable'


class Visit(models.Model):
    visit_num = models.PositiveIntegerField(db_column='VISIT_NUM', primary_key=True)
    visit_date = models.DateField(db_column='VISIT_DATE')
    visit_visitor = models.CharField(db_column='VISIT_VISITOR', max_length=4)
    visit_leavehour = models.PositiveIntegerField(db_column='VISIT_LEAVEHOUR')
    student_stu_num = models.ForeignKey(Student, models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')

    def __str__(self):
        return f"{self.student_stu_num.stu_name} {self.visit_date}"

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'visit'


class recommendclass(models.Model):
    rec_num = models.PositiveIntegerField(db_column='rec_num', primary_key=True)
    rec_classtype = models.CharField(db_column='rec_classtype', max_length=10)
    rec_class = models.CharField(db_column='rec_class', max_length=20)
    rec_pro = models.CharField(db_column='rec_pro', max_length=20)
    rec_price = models.PositiveIntegerField(db_column='price per hour')
    rec_weightpl = models.FloatField(db_column='rec_weightpl')
    rec_weightmi = models.FloatField(db_column='rec_weightmi')

    class Meta:
        managed = True
        db_table = 'recommendclass'
