
from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.urls import include, path
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'usersapi', views.UserViewSet)
router.register(r'adminapi', views.AdminViewSet)
router.register(r'studentapi', views.StudentViewSet)
router.register(r'facultyapi', views.FacultyViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]