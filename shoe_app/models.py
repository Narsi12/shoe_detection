from django.db import models

class ShoeType(models.Model):
    shoe_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.shoe_type

class Product(models.Model):
    name = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, related_name='products')
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    count = models.IntegerField()
    product_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name