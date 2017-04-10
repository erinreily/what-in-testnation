from __future__ import unicode_literals
from django.db import models


class Donation(models.Model):
<<<<<<< HEAD
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=False, blank=False)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    cvv = models.CharField(max_length=4, null=True, blank=False)
    message = models.TextField(null=True, blank=True)
    donation_made = models.DateTimeField(null=True, blank=False)

    def __str__(self):
        to_string = "Donation of: $" + str(self.amount)
        if self.first_name or self.last_name:
            to_string += " by "
            if self.first_name:
                to_string += self.first_name + " "
            if self.last_name:
                to_string += self.last_name

        return to_string

=======
    name = models.CharField(max_length=150, null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=False, blank=False)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    message = models.TextField()
    donation_made = models.DateTimeField
    def __str__(self):
        return "Donation by: " + self.name + " of: $" + self.amount
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
