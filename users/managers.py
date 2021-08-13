from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for authentication rather than a username.
    """

    def create_user(self, email, password, **kwargs):
        """
        Create and save a user with an email and a password.
        """
        if not email:
            raise ValueError(gettext_lazy('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Create and save a super user inheriting create_user
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **kwargs)
