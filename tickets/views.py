from rest_framework import generics
from .models import Customer, Purchase
from .serializers import CustomerSerializer, PurchaseSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.none()
    serializer_class = CustomerSerializer

class PurchaseListCreate(generics.ListCreateAPIView):
    queryset = Purchase.objects.none()
    serializer_class = PurchaseSerializer
