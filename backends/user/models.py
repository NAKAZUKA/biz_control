from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=15,
                                    blank=True,
                                    null=True,
                                    unique=True,
                                    verbose_name='Номер телефона')
    role = models.CharField(
        max_length=50,
        choices=[
            ('staff', 'Staff'),
            ('manager', 'Manager'),
            ('admin', 'Admin'),
            ('customer', 'Customer'),
            ('owner', 'Owner'),
            ('director', 'Director'),
            ('supplier', 'Supplier'),
        ],
        default='staff',
        null=True,
        blank=True,
        verbose_name='Роль в компании')
    specialty = models.CharField(max_length=50,
                                 blank=True,
                                 null=True,
                                 verbose_name='Специальность')
    position = models.CharField(max_length=50,
                                blank=True,
                                null=True,
                                verbose_name='Должность')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
