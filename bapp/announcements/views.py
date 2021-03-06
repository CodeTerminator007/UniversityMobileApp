from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Announcement
from .serializer import AnnouncementSerializer
from rest_framework.parsers import FormParser, MultiPartParser

class AnnouncementView(viewsets.ModelViewSet):

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    parser_classes = (MultiPartParser, FormParser)
