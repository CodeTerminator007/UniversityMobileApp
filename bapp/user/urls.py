
from posixpath import basename
from django.urls import include, path
from rest_framework import  routers
from user import views
from .views import LoginView

router = routers.DefaultRouter()
router.register(r'allusers', views.UserViewSet)
router.register(r'admin', views.AdminViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'faculty', views.FacultyViewSet)

# router.register(r'addUser',views.CreateUserviewset,basename='MyModel')


urlpatterns = [
    path('login', LoginView.as_view()),
    path('', include(router.urls)),
    
]