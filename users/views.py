from django.contrib.auth import logout
from django.core.validators import validate_email
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.serializers import UserSerializer


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def create_superuser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        raise ValidationError(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def delete_user(request):
    user = request.user

    # Logout before we delete. This will make request.user
    # unavailable (or actually, it points to AnonymousUser).
    logout(request)

    # Delete user (and any associated ForeignKeys, according to
    # on_delete parameters).
    user.delete()

    return Response("Account successfully deleted!")
