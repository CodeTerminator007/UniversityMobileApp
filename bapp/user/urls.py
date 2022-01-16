
from email.mime import base
from posixpath import basename
from django.urls import include, path
from rest_framework import  routers
from user import views
from .views import LoginView
from announcements.views import AnnouncementView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user/admin', views.AdminViewSet)
router.register(r'user/student', views.StudentViewSet)
router.register(r'user/faculty', views.FacultyViewSet)
router.register(r'announcement',AnnouncementView)

# router.register(r'addUser',views.CreateUserviewset,basename='MyModel')


urlpatterns = [
    path('auth/login', LoginView.as_view()),
    path('', include(router.urls)),
    
]