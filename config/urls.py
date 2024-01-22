from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    info=openapi.Info(
        title='TODO API Documentation',
        default_version='v1',
        description='TODO APPLICATION API DOCUMENTATION',
        terms_of_service='https://www.google.com',
        contact=openapi.Contact(email='test.email@example.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=([AllowAny])
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.router')),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0)
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui('swagger', cache_timeout=0)
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui('redoc', cache_timeout=0)
    ),
]
