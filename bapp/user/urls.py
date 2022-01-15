
from django.urls import include, path
from rest_framework import  routers
from user import views


router = routers.DefaultRouter()
router.register(r'allusers', views.UserViewSet)
router.register(r'admin', views.AdminViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'faculty', views.FacultyViewSet)
# router.register(r'addUser',views.CreateUserviewset,basename='MyModel')


urlpatterns = [
  
    path('', include(router.urls)),
    
]