from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models



class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    fines = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username