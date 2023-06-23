
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dsp-admin/', admin.site.urls),
    path('', include('dinamo_app_gerente.urls'))
]
