from encodings import utf_8

import jwt
from django.conf import settings
from django.contrib import auth
from django.db.models import Case, Count, F, When
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

import user
from user import serializer

from .models import (Admin, Assignment, AssignmentResult, AssignmentSubmission,
                     Attendance, AttendanceReport, Faculty, Question, Quiz,
                     QuizResult, Result, Student, SubjectResult, Timetable,
                     User, incorrect_answers)
from .serializer import (AdminSerializer, Assignmentmarkserializer,
                         AssignmentSerializer, AssignmentSubmissionSerializer,
                         AttendanceReportSerializer, AttendanceSerializer,
                         BulkAttandanceSerializer, FacultyalleditSerializer,
                         FacultySerializer, LoginSerializer,
                         QuestionSerializer, QuizResultscreenSerializer,
                         QuizResultSerializer, QuizSerializer,
                         ResultSerializer, SecondAssignmentSerializer,
                         StudentalleditSerializer,
                         StudentAttendanceReportSeralizer,
                         StudentPostSerializer, StudentSerializer,
                         SubjectResultSerializer, TimetableSerializer,
                         UserSerializer, UserUpdatewithoutpasswwordSerializer,
                         incorrect_answersSerializer)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            serializer = UserSerializer(user)
            data = {'user':serializer.data,'jwt': get_tokens_for_user(user)}
            return Response(data, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


class UserUpdatewithoutpasswordViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserUpdatewithoutpasswwordSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentpostViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = StudentPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)




class AdminViewSet(viewsets.ModelViewSet):

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def retrieve(self,request,*args,**kwargs):
        studentes = Student.objects.filter(the_class = kwargs['pk'])
        serializer = StudentSerializer(studentes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    


class SimpleStudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class Studentalleditviewset(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentalleditSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


class Facultualleditviewset(viewsets.ModelViewSet):

    queryset = Faculty.objects.all()
    serializer_class = FacultyalleditSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

class NormalStudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class FacultyViewSet(viewsets.ModelViewSet):

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('class_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))
@method_decorator(name='student_attendance_report', decorator=swagger_auto_schema(
    responses={'200': StudentAttendanceReportSeralizer()}
))
class AttendanceViewSet(viewsets.ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            class_id = self.request.query_params.get('class_id', None)
            subject_id = self.request.query_params.get('subject_id', None)
            if class_id and subject_id:
                return super().get_queryset().filter(class_id=class_id, subject_id=subject_id)
        return super().get_queryset()
    
    @action(methods=['GET'], detail=True)
    def student_attendance_report(self, request, pk=None):
        total_data = Attendance.objects.all().values('class_id', 'subject_id__subject_name', 'subject_id__staff_id__username').annotate(total_lectures=Count('id'))
        report_data = AttendanceReport.objects.filter(student_id_id=pk).values(
        CourseName=F('subject_id__subject_name'),
        TeacherName=F('subject_id__staff_id__username')
        ).annotate(total_present=Count(
            Case(
                When(
                    status=True,
                    then=1
            ))),
            total_absent=Count(Case(When(status=False,then=1)))
            )
        subject_total_lecure_map =  {}

        for x in total_data:
            subject_total_lecure_map[x['subject_id__subject_name']] = x['total_lectures']

        for x in report_data:
            x['Lectures']=subject_total_lecure_map[x['CourseName']]
            x['Percentage'] =  (x['total_present'] / subject_total_lecure_map[x['CourseName']])*100

        return Response(report_data)



class AttendanceReportViewSet(viewsets.ModelViewSet):

    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
class TimeTableViewSet(viewsets.ModelViewSet):

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def retrieve(self,request,*args,**kwargs):
        timetable = Timetable.objects.filter(person = kwargs['pk'])
        serializer = TimetableSerializer(timetable,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))
class BulkattandanceView(BulkModelViewSet):
    queryset = AttendanceReport.objects.all()
    serializer_class = BulkAttandanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    def get_queryset(self):
        if self.action == 'list':
            student_id = self.request.query_params.get('student_id', None)
            subject_id = self.request.query_params.get('subject_id', None)
            if student_id and subject_id:
                return super().get_queryset().filter(student_id=student_id, subject_id=subject_id)
        return super().get_queryset()    



class AssignmentViewSet(viewsets.ModelViewSet):

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    
    def retrieve(self,request,*args,**kwargs):
        assignment = Assignment.objects.filter(subject = kwargs['pk'])
        serializer = AssignmentSerializer(assignment,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class SecondAssignmentViewSet(viewsets.ModelViewSet):

    queryset = Assignment.objects.all()
    serializer_class = SecondAssignmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('assignment', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))

class AssignmentSubmissionViewSet(viewsets.ModelViewSet):

    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    parser_classes = (MultiPartParser, FormParser)
    def get_queryset(self):
        if self.action == 'list':
            student_id = self.request.query_params.get('student_id', None)
            assignment = self.request.query_params.get('assignment', None)
            if student_id and assignment:
                return super().get_queryset().filter(student=student_id, assignment=assignment)
        return super().get_queryset()    

@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('subject_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))

class AssignmentmarksresultViewSet(viewsets.ModelViewSet):

    queryset = AssignmentResult.objects.all()
    serializer_class = Assignmentmarkserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    def get_queryset(self):
        if self.action == 'list':
            student_id = self.request.query_params.get('student_id', None)
            subject_id = self.request.query_params.get('subject_id', None)
            if student_id and subject_id:
                return super().get_queryset().filter(student=student_id, subject=subject_id)
        return super().get_queryset()   

class SecondAssignmentSubmissionViewSet(viewsets.ModelViewSet):

    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    parser_classes = (MultiPartParser, FormParser)

    def retrieve(self,request,*args,**kwargs):
        assignmentsub = AssignmentSubmission.objects.filter(assignment = kwargs['pk'])
        serializer = AssignmentSubmissionSerializer(assignmentsub,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('subject_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))
class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            subject_id = self.request.query_params.get('subject_id', None)
            if subject_id:
                return super().get_queryset().filter(subject=subject_id)
        return super().get_queryset()    

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class incorrect_answerViewSet(viewsets.ModelViewSet):

    queryset = incorrect_answers.objects.all()
    serializer_class = incorrect_answersSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



@method_decorator(name='retrieve', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))
class QuizResultViewSet(viewsets.ModelViewSet):

    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self,request,*args,**kwargs):

        student_id = self.request.query_params.get('student_id', None)
        quizresult = QuizResult.objects.filter(quiz = kwargs['pk'],student=student_id)
        serializer = QuizResultSerializer(quizresult,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('subject', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))

class quizresultscreenviewset(viewsets.ModelViewSet):

    queryset = QuizResult.objects.all()
    serializer_class = QuizResultscreenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    def get_queryset(self):
        if self.action == 'list':
            student_id = self.request.query_params.get('student_id', None)
            subject = self.request.query_params.get('subject', None)
            if student_id and subject:
                return super().get_queryset().filter(student=student_id, subject=subject)
        return super().get_queryset()    



@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[
        openapi.Parameter('student_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
    ]))

class ResultViewset(viewsets.ModelViewSet):

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.action == 'list':
            student_id = self.request.query_params.get('student_id', None)
            if student_id :
                return super().get_queryset().filter(student=student_id)
        return super().get_queryset()    




class SubjectResultViewset(viewsets.ModelViewSet):

    queryset = SubjectResult.objects.all()
    serializer_class = SubjectResultSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]