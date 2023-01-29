from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from auth_django.models import User
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model  # If used custom user model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

from auth_django.validators import validateUser

# UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer para registro """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password',
                  'email')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)

#     def create(self, validated_data):

#         user = UserModel.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )

#         return user

#     class Meta:
#         model = UserModel
#         # Tuple of serialized model fields (see link [2])
#         fields = ("id", "username", "password", )


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     """ Serializer Token do JWT """

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         return token


class ChangePasswordSerializer(serializers.Serializer):
    """ Serializer para alterar senha """
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, write_only=True)
    username = serializers.EmailField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=68, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        for k, v in validateUser.validadores_usuarios.items():
            v(user)

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
