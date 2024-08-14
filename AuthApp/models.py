from django.db import models
from django.utils import timezone

class UserPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=6, blank=True, null=True)
    password_expiry = models.DateTimeField(blank=True, null=True)

    def is_password_valid(self, password):
        return self.password == password and timezone.now() < self.password_expiry
