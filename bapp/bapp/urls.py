
from django.contrib import admin
from django.urls import include, path ,re_path
from user import urls
from rest_framework_simplejwt import views as jwt_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Riphah University Api",
      default_version='v1',
      description="Platform for myself to test apis here",
      terms_of_service="https://www.riphahfsd.com",
      contact=openapi.Contact(email="Husnain@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),        
    path('admin/', admin.site.urls),    
    path('',include(urls)),
  
]



