from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('staff', 'Staff'),
            ('manager', 'Manager'),
            ('admin', 'Admin'),
            ('customer', 'Customer'),
            ('owner', 'Owner')
        ],
        default='staff',
        null=True,
        blank=True)
    specialty = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
