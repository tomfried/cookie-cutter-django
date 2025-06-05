from django.db import models


class Balance(models.Model):
    # Fields
    address = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(default="current", max_length=10)
    date = models.DateTimeField(auto_now_add=True)
