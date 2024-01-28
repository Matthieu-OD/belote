from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, username: str, password: str,
                    **extra_fields) -> "get_user_model()":
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")

        email = self.normalize._email(email)
        user = self.model(email=email, username=username, password=password)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, username: str, password: str,
                         **extra_fields) -> "get_user_model()":
        extra_fields.set_default("is_staff", True)
        extra_fields.set_default("is_superuser", True)

        if extra_fields.get("is_staff", True):
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser", True):
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email


class Player(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
