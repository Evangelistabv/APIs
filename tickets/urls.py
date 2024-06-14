from django.urls import path
from .views import CustomerListCreate, PurchaseListCreate

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('purchases/', PurchaseListCreate.as_view(), name='purchase-list-create'),
]