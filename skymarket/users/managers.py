from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    """ Собственный класс Manager """

    def create_user(self, email, password=None):
        """ Создает и возвращает пользователя с email, паролем """

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Создает и возвращает пользователя с привилегиями superuser """

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'admin'
        user.save()

        return user
