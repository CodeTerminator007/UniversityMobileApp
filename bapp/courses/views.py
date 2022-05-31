from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets ,status
from rest_framework.response import Response
from user.models import Subjects
from user.models import Courses ,Class
from .serializer import CourseSerializer , ClassSerializer
from .serializer import SubjectsSerializer




class CourseViewset(viewsets.ModelViewSet):

    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class SubjectsViewset(viewsets.ModelViewSet):

    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def retrieve(self,request,*args,**kwargs):
        timetable = Subjects.objects.filter(staff_id = kwargs['pk'])
        serializer = SubjectsSerializer(timetable,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class SubjectsViewsetfilterclass(viewsets.ModelViewSet):

    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def retrieve(self,request,*args,**kwargs):
        timetable = Subjects.objects.filter(class_id = kwargs['pk'])
        serializer = SubjectsSerializer(timetable,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    

class ClassViewset(viewsets.ModelViewSet):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



