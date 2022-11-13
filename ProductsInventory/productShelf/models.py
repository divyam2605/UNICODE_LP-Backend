from django.db import models

# Create your models here.

class products(models.Model):
    product_id = models.IntegerField()
    productname = models.CharField(max_length=30)
    companyname = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_left = models.IntegerField()

    def __str__(self):
        return self.productname
