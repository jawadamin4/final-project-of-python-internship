from django.db import models


class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    last_price = models.CharField(max_length=20)
    change = models.CharField(max_length=20)
    percentage_change = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.symbol} - {self.name}"
