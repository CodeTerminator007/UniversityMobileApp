
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from user import urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api',include(urls))
]