from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=30)

    class Meta:
        db_table = 'Products'
