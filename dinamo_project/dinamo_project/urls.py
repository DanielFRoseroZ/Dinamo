
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('dsp-admin/', admin.site.urls),
    path('', include('dinamo_app_gerente.urls')),
    path('', include('Token.urls')),
]
