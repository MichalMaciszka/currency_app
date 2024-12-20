from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=7, unique=False)
    exchange_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency_pair} - {self.exchange_rate} on {self.timestamp}"
