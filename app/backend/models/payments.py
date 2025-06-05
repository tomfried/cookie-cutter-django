from django.db import models


class Payment(models.Model):
    # Fields
    address = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    type = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
