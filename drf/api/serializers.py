import re

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'mmr']


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        self.validate_username_field(attrs['username'])
        return attrs

    def validate_username_field(self, username):
        if len(username) < 3 or len(username) > 18:
            raise serializers.ValidationError(
                {"username": "Имя пользователя должно быть от 3 до 18 символов."}
            )

        if not re.match("^[a-zA-Z0-9_]*$", username):
            raise serializers.ValidationError(
                {"username": "Имя пользователя может содержать только латинские буквы, цифры и символ '_'"}
            )

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": "Пользователь с таким именем уже существует."}
            )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
