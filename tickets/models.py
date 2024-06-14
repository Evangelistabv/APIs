from django.db import models

class Customer(models.Model):
    name_customer = models.CharField(max_length=100)
    email_customer = models.EmailField(max_length=100)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.id}"

class Purchase(models.Model):
    id_ticket = models.ForeignKey(Customer, related_name='purchases', on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_product = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product}"
