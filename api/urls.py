from django.urls import path
from .views import saludo

urlpatterns = [
    path('mensaje/<str:nombre>/', saludo, name='saludo')
]
