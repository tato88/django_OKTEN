from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

from .managers import UserManager

from .enums import RegEx
from .services import upload_to


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, validators=[
        RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)
    ])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    phone = models.CharField(max_length=10, validators=[RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    avatar = models.ImageField(upload_to=upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
