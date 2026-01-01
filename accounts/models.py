from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser, PermissionsMixin):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    username = None
    email = models.EmailField(verbose_name='электронная почта', unique=True, blank=False, null=False)
    phone_number = PhoneNumberField(verbose_name='Номер телефона', null=True, blank=True)
    full_name = models.CharField(max_length=200, verbose_name='ФИО')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return self.email


class PasswordResetCode(models.Model):
    email = models.EmailField(verbose_name='Электроная почта', null=True, blank=True)
    code = models.CharField(max_length=4)
    expires_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.expires_at
    
    @staticmethod
    def create_code(user):
        from random import randint
        return PasswordResetCode.objects.create(
            user=user,
            code=str(randint(1000, 9999)),
            expires_at=timezone.now() + timedelta(minutes=5)
        )
