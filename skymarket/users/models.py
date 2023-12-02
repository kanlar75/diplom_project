from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    USER = 'user', _('user')  # Пользователь
    ADMIN = 'admin', _('admin')  # Админ


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=250, unique=True,
                              verbose_name='Адрес электронной почты')
    first_name = models.CharField(max_length=100, **NULLABLE,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=100, **NULLABLE,
                                 verbose_name='Фамилия')
    image = models.ImageField(upload_to='users/', **NULLABLE,
                              verbose_name='Аватар')
    phone = PhoneNumberField('Телефон', unique=True, **NULLABLE)
    role = models.CharField(max_length=10, choices=UserRoles.choices,
                            default=UserRoles.USER,
                            verbose_name='Роль пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
