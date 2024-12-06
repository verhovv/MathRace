import re

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User, Car


def validate_username_field(username):
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


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'mmr']


class UserSerializer(serializers.ModelSerializer):
    imgCar = serializers.SlugRelatedField(source='car', slug_field='image_path', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'mmr', 'imgCar']


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

        validate_username_field(attrs['username'])
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            car=Car.objects.order_by('mmr_bound').first()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class ChangeUsernameSerializer(serializers.Serializer):
    new_username = serializers.CharField(required=True)

    def validate(self, attrs):
        validate_username_field(attrs['new_username'])
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        user = self.context['request'].user

        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Неверный старый пароль"})

        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password": "Новые пароли не совпадают"})

        if user.check_password(attrs['new_password']):
            raise serializers.ValidationError({"new_password": "Новый пароль не должен совпадать со старым"})

        return attrs
