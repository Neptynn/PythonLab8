from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=50)
    account_number = models.CharField(max_length=120, unique=True)
    class Meta: db_table = 'Clients'

    def __str__(self):
        return self.client_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    class Meta: db_table = 'Product'

    def __str__(self):
        return self.product_name

class Sale(models.Model):
    sale_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    payment_form = models.CharField(max_length=15)
    delivery_needed = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta: db_table = 'Sales'

    def __str__(self):
        return f"{self.client} - {self.product}"
