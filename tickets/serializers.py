from rest_framework import serializers
from .models import Customer, Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'id_ticket', 'product', 'quantity', 'total_product']
    def validate(self, data):
        customer = data['id_ticket']
        total_product = data['total_product']
        total_purchase_sum = sum(p.total_product for p in customer.purchases.all()) + total_product

        if total_purchase_sum > customer.total_compra:
            raise serializers.ValidationError(
                f"Total de productos para el cliente {customer.id} supera el total de compra permitido ({customer.total_compra})."
            )
        
        return data

class CustomerSerializer(serializers.ModelSerializer):
    purchases = PurchaseSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'name_customer', 'email_customer', 'total_compra', 'date', 'purchases']