from django.urls import path
from .views import ObtainToken,CheckToken

#URLs de la app Token
urlpatterns = [
    path('login/', ObtainToken.as_view(), name="token_obtain_pair"),
    path('checkToken/',CheckToken.as_view()),
] 

