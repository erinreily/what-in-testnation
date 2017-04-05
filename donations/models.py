from __future__ import unicode_literals
from django.db import models


class Donation(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=False, blank=False)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    message = models.TextField()
    donation_made = models.DateTimeField
    def __str__(self):
        return "Donation by: " + self.name + " of: $" + self.amount
