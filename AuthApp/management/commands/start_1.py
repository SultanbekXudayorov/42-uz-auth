import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from AuthApp.models import UserPhoneNumber

class Command(BaseCommand):
    help = 'Telfon raqam uchun 6-xonali parol yaratish'

    def handle(self, *args, **kwargs):
        phone_number = input("Enter your phone number: ")
        user_phone, created = UserPhoneNumber.objects.get_or_create(phone_number=phone_number)

        password = random.randint(100000, 999999)
        expiry_time = timezone.now() + timedelta(minutes=2)

        user_phone.password = password
        user_phone.password_expiry = expiry_time
        user_phone.save()

        self.stdout.write(f"Your 6-digit password is: {password}")
        self.stdout.write(f"The password is valid until: {expiry_time}")
