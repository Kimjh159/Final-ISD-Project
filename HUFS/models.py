from django.db import models

class Administrator(models.Model):
    admin_num = models.PositiveIntegerField(db_column='ADMIN_NUM', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='ADMIN_NAME', max_length=4)  # Field name made lowercase.
    admin_age = models.PositiveIntegerField(db_column='ADMIN_AGE')

    def __str__(self):
        return self.admin_name

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'administrator'


class Class(models.Model):
    class_type = models.CharField(db_column='CLASS_TYPE', primary_key=True, max_length=2)  # Field name made lowercase.
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')

    def __str__(self):
        return self.class_type

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'class'


class Counseling(models.Model):
    cou_num = models.PositiveIntegerField(db_column='COU_NUM', primary_key=True)  # Field name made lowercase.
    cou_date = models.DateField(db_column='COU_DATE')  # Field name made lowercase.
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')  # Field name made lowercase.
    student_stu_num = models.ForeignKey('Student', models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')

    def __str__(self):
        return f"{self.cou_date} {self.student_stu_num.stu_name}"

    class Meta:
        managed = True
        db_table = 'counseling'


class MockTest(models.Model):
    mock_id = models.PositiveIntegerField(db_column='MOCK_ID', primary_key=True)
    mock_kor = models.PositiveIntegerField(db_column='MOCK_KOR')  # Field name made lowercase.
    mock_math = models.PositiveIntegerField(db_column='MOCK_MATH')  # Field name made lowercase.
    mock_eng = models.PositiveIntegerField(db_column='MOCK_ENG')  # Field name made lowercase.
    mock_extraclass_1 = models.PositiveIntegerField(db_column='MOCK_EXTRACLASS_1')  # Field name made lowercase.
    mock_extraclass_2 = models.PositiveIntegerField(db_column='MOCK_EXTRACLASS_2')  # Field name made lowercase.
    date = models.TextField()
    student_stu_num = models.ForeignKey('Student', models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')  # Field name made lowercase.

    def __str__(self):
        return f"{self.student_stu_num}{self.date}"

    class Meta:
        managed = True
        db_table = 'mock_test'


class Room(models.Model):
    room_num = models.PositiveIntegerField(db_column='ROOM_NUM', primary_key=True)  # Field name made lowercase.
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')  # Field name made lowercase.

    def __str__(self):
        return f" {self.room_num}"

    class Meta:
        managed = True
        db_table = 'room'


class Student(models.Model):
    stu_num = models.PositiveIntegerField(db_column='STU_NUM', primary_key=True)  # Field name made lowercase.
    stu_name = models.CharField(db_column='STU_NAME', max_length=4)  # Field name made lowercase.
    stu_age = models.PositiveIntegerField(db_column='STU_AGE')  # Field name made lowercase.
    stu_sex = models.CharField(db_column='STU_SEX', max_length=1)  # Field name made lowercase.
    stu_birth = models.DateField(db_column='STU_BIRTH')  # Field name made lowercase.
    stu_curriculum = models.CharField(db_column='STU_CURRICULUM', max_length=1)  # Field name made lowercase.
    stu_extraclass_1 = models.CharField(db_column='STU_EXTRACLASS_1', max_length=2)  # Field name made lowercase.
    stu_extraclass_2 = models.CharField(db_column='STU_EXTRACLASS_2', max_length=2)  # Field name made lowercase.
    stu_formerexam = models.DecimalField(db_column='STU_FORMEREXAM', max_digits=3,
                                         decimal_places=2)  # Field name made lowercase.
    stu_leave_date = models.DateField(db_column='STU_LEAVE_DATE')  # Field name made lowercase.
    stu_leave_reason = models.CharField(db_column='STU_LEAVE_REASON', max_length=100)  # Field name made lowercase.
    room_room_num = models.ForeignKey(Room, models.DO_NOTHING, db_column='ROOM_ROOM_NUM')  # Field name made lowercase.
    class_class_type = models.ForeignKey(Class, models.DO_NOTHING,
                                         db_column='CLASS_CLASS_TYPE')

    def __str__(self):
        return f"{self.stu_num} {self.stu_name}"

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'student'


class Teacher(models.Model):
    tea_num = models.PositiveIntegerField(db_column='TEA_NUM', primary_key=True)  # Field name made lowercase.
    tea_name = models.CharField(db_column='TEA_NAME', max_length=4)  # Field name made lowercase.
    tea_age = models.PositiveIntegerField(db_column='TEA_AGE')  # Field name made lowercase.
    tea_sex = models.CharField(db_column='TEA_SEX', max_length=1)  # Field name made lowercase.
    tea_subject = models.CharField(db_column='TEA_SUBJECT', max_length=2)

    def __str__(self):
        return f"{self.tea_subject} {self.tea_name}"

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'teacher'


class Timetable(models.Model):
    tita_num = models.PositiveIntegerField(db_column='TITA_NUM', primary_key=True)  # Field name made lowercase.
    tita_day = models.CharField(db_column='TITA_DAY', max_length=1)  # Field name made lowercase.
    tita_1c = models.CharField(db_column='TITA_1C', max_length=2)  # Field name made lowercase.
    tita_2c = models.CharField(db_column='TITA_2C', max_length=2)  # Field name made lowercase.
    tita_3c = models.CharField(db_column='TITA_3C', max_length=2)  # Field name made lowercase.
    tita_4c = models.CharField(db_column='TITA_4C', max_length=2)  # Field name made lowercase.
    class_class_type = models.ForeignKey(Class, models.DO_NOTHING,
                                         db_column='CLASS_CLASS_TYPE')

    def __str__(self):
        return f"{self.tita_day} {self.class_class_type.class_type}"

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'timetable'


class Visit(models.Model):
    visit_num = models.PositiveIntegerField(db_column='VISIT_NUM', primary_key=True)  # Field name made lowercase.
    visit_date = models.DateField(db_column='VISIT_DATE')  # Field name made lowercase.
    visit_visitor = models.CharField(db_column='VISIT_VISITOR', max_length=4)  # Field name made lowercase.
    visit_leavehour = models.PositiveIntegerField(db_column='VISIT_LEAVEHOUR')  # Field name made lowercase.
    student_stu_num = models.ForeignKey(Student, models.DO_NOTHING,
                                        db_column='STUDENT_STU_NUM')  # Field name made lowercase.
    administrator_admin_num = models.ForeignKey(Administrator, models.DO_NOTHING,
                                                db_column='ADMINISTRATOR_ADMIN_NUM')

    def __str__(self):
        return f"{self.student_stu_num.stu_name} {self.visit_date}"

    # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'visit'
