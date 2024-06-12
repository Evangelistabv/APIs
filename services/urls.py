from django.urls import path
from .views import ServiceCreate

urlpatterns = [
    path('services/', ServiceCreate.as_view(), name='servicio-create'),
]