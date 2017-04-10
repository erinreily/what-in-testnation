from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wage = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    title = models.CharField(max_length=40)
    supervisor = models.ForeignKey("self", null=True, blank=True, related_name="subortinates")

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def get_subordinates(self):
        return Staff.objects.filter(parent=self)

    @property
    def has_subordinates(self):
        if not Staff.objects.filter(parent=self):
            return False
        return True
