from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
