from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

from users.managers import CustomUserManager


class Employee(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy('email address'), unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
