from rest_framework import serializers
from users.models import Employee
from django.core.validators import validate_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
        ]
