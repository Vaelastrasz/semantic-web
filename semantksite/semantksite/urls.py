from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('Social/', include('Social.urls', namespace='Social')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title='Social web',
            default_version='v1',
            description='Social web network',
            contact=openapi.Contact(email='chobanitsavlad@gmail.com'),
            license=openapi.License(name='Google License'),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

