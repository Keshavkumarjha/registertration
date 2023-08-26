from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    full_name = models.CharField(_('full name'), max_length=255)
    phone_number = PhoneNumberField(_('phone number'), max_length=20)

    def __str__(self):
        return self.username
