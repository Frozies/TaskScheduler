from rest_framework import serializers
from users.models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name']
