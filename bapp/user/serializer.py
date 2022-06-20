from dataclasses import fields
from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import Permission
from pyexpat import model
from rest_framework import serializers
from rest_framework_bulk import (BulkListSerializer, BulkSerializerMixin,
                                 ListBulkCreateUpdateDestroyAPIView)

from .models import (Admin, Assignment, AssignmentResult, AssignmentSubmission,
                     Attendance, AttendanceReport, Faculty, Question, Quiz,
                     QuizResult, Result, Student, SubjectResult, Timetable,
                     User, incorrect_answers)

from drf_extra_fields.fields  import Base64FileField

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    class Meta:
        model = User 
        fields = ['id','username','email','password','first_name','last_name','is_admin','is_student','is_faculty','phone_number1','phone_number2','gender','last_education_degree','Dob','cnic','profile_image']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdatewithoutpasswwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username','email','first_name','last_name','phone_number1','phone_number2','gender','last_education_degree','Dob','cnic']
        
class StudentPostSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)
    course = serializers.CharField(source='course_id.course_name')
    the_class = serializers.CharField(source='the_class.class_name')
    address = serializers.CharField(max_length=600,allow_blank=True)
    class Meta:
        model = User 
        fields = ['id','username','email','password','first_name','last_name','is_admin','is_student','is_faculty','phone_number1','phone_number2','gender','last_education_degree','Dob','cnic','profile_image','course','the_class','address']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        

class AdminSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    Dob = serializers.ReadOnlyField(source='user.Dob')
    phone_number1 = serializers.ReadOnlyField(source='user.phone_number1')
    phone_number2 = serializers.ReadOnlyField(source='user.phone_number2')
    gender = serializers.ReadOnlyField(source='user.gender')
    last_education_degree = serializers.ReadOnlyField(source='user.last_education_degree')
    cnic = serializers.ReadOnlyField(source='user.cnic')
    profile_image = serializers.ImageField(required=False,source='user.profile_image')

    class Meta:
        model = Admin 
        fields = ['first_name','last_name','username','user','email','Dob','gender','phone_number1','phone_number2','last_education_degree','cnic','profile_image']

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')


    class Meta:
        model = Student 
        fields = '__all__'


class StudentalleditSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    Dob = serializers.ReadOnlyField(source='user.Dob')
    phone_number1 = serializers.ReadOnlyField(source='user.phone_number1')
    phone_number2 = serializers.ReadOnlyField(source='user.phone_number2')
    gender = serializers.ReadOnlyField(source='user.gender')
    last_education_degree = serializers.ReadOnlyField(source='user.last_education_degree')
    cnic = serializers.ReadOnlyField(source='user.cnic')
    profile_image = serializers.ImageField(required=False,source='user.profile_image')
    course = serializers.CharField(source='course_id.course_name')
    classs = serializers.CharField(source='the_class.class_name')
    semaster = serializers.CharField(source='the_class.semaster')
    sec = serializers.CharField(source='the_class.sec')

    class Meta:
        model = Student 
        fields = ['first_name','last_name','username','email','Dob','phone_number1','phone_number2','gender','last_education_degree','cnic','profile_image','user','address','the_class','course_id','course','classs','semaster','sec']


class FacultyalleditSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    Dob = serializers.ReadOnlyField(source='user.Dob')
    phone_number1 = serializers.ReadOnlyField(source='user.phone_number1')
    phone_number2 = serializers.ReadOnlyField(source='user.phone_number2')
    gender = serializers.ReadOnlyField(source='user.gender')
    last_education_degree = serializers.ReadOnlyField(source='user.last_education_degree')
    cnic = serializers.ReadOnlyField(source='user.cnic')
    profile_image = serializers.ImageField(required=False,source='user.profile_image')


    class Meta:
        model = Faculty 
        fields = ['first_name','last_name','username','email','Dob','phone_number1','phone_number2','gender','last_education_degree','cnic','profile_image','user']


class FacultySerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    
    class Meta:
        model = Faculty 
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255,min_length=2)
    password = serializers.CharField(max_length=65,min_length=8,write_only=True)
    class Meta:
        model = User
        fields = ['username','password']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance 
        fields = '__all__'

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = '__all__'
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'


class BulkAttandanceSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        list_serializer_class = BulkListSerializer
        fields = '__all__'

class StudentAttendanceReportSeralizer(serializers.Serializer):
    CourseName = serializers.CharField()
    TeacherName = serializers.CharField()
    Lectures = serializers.IntegerField()
    Present = serializers.IntegerField()
    Absents = serializers.IntegerField()
    Percent = serializers.IntegerField()


class AssignmentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(required=False)
    class Meta:
        model =  Assignment
        fields =  ['id','faculty','Title','detail','submission_date','submission_time','document','subject','status','marks','class_id']

class SecondAssignmentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(required=False)
    class Meta:
        model =  Assignment
        fields =  ['id','faculty','Title','detail','submission_date','submission_time','document','subject','status','marks','class_id']

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='student.user.first_name')
    last_name = serializers.ReadOnlyField(source='student.user.last_name')
    roll_no = serializers.ReadOnlyField(source='student.roll_num')
    document = serializers.FileField(required=False)
    document2 = Base64FileField(source='document')

    class Meta:
        model =  AssignmentSubmission
        fields =  ['id','assignment','student','document','comment','marks','submission_datetime','first_name','last_name','roll_no','document2']

class Assignmentmarkserializer(serializers.ModelSerializer):

    totalmarks = serializers.ReadOnlyField(source='assignment.marks')
    assignment_name = serializers.ReadOnlyField(source='assignment.Title')

    class Meta:
        model =  AssignmentResult
        fields =  ['id','assignment','student','marks','totalmarks','subject','assignment_name']


class incorrect_answersSerializer(serializers.ModelSerializer):
    class Meta:
        model = incorrect_answers
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    incorrect_answers = incorrect_answersSerializer(many=True, read_only=True)    
    class Meta:
        model = Question
        fields = ['id','question','quiz','correct_answer','incorrect_answers']

class QuizSerializer(serializers.ModelSerializer):
    allquestions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id','title','subject','time','quizDate','allquestions']


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult 
        fields = '__all__'

class QuizResultscreenSerializer(serializers.ModelSerializer):
    quiz_name = serializers.ReadOnlyField(source='quiz.title')

    class Meta:
        model = QuizResult 
        fields = ['id','quiz_name','quiz','student','marks','subject','outofmarks']
        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result 
        fields = '__all__'

class SubjectResultSerializer(serializers.ModelSerializer):
    subjectname = serializers.ReadOnlyField(source='subject.subject_name')
    teacherfirstname = serializers.ReadOnlyField(source='subject.staff_id.first_name')    
    teacherlastname = serializers.ReadOnlyField(source='subject.staff_id.last_name')    
    
    class Meta:
        model = SubjectResult 
        fields = ['subjectname','teacherfirstname','teacherlastname','classid','student','subject','result','midobtainedMarks','finalobtainedMarks','sessionalmarks','id']
