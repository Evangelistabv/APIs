from django.urls import path
from .views import ServiceCreate

urlpatterns = [
    path('servicios/', ServiceCreate.as_view(), name='servicio-create'),
]