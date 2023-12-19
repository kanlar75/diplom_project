from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    """ Собственный класс Manager """

    def create_user(self, email, first_name=None, last_name=None, phone=None,
                    password=None, is_active='True', role='user'):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            is_active=is_active
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Создает и возвращает пользователя с привилегиями superuser """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.role = 'admin'
        user.set_password(password)
        user.save(using=self._db)

        return user

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'
