from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    USER = 'user', _('user')  # Пользователь
    ADMIN = 'admin', _('admin')  # Админ


class User(AbstractBaseUser):
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
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
