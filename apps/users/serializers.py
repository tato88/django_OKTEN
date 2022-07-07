from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer, ValidationError

from apps.users.models import ProfileModel, UserModel

UserModel: Type[UserModel] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class AddAvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at',
                  'updated_at', 'profile')
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at',
                            'updated_at', 'profile')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        if email == password:
            raise ValidationError('email eq password')
        return super().validate(attrs)

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
