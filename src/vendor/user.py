from uuid import uuid4

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    """
    Manager class for user, helps in creation
    of regular and superusers.

    """

    def create_user(self, email, first_name, last_name, password, **options):
        if not email:
            raise ValueError(" Users must have email ")

        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **options
        )
        if password:
            user.set_password(password)
        user.email_verified = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **options):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **options,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model, for email and Oauth with
    additional custom information
    """

    uid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
        unique=True,
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    user_role = models.CharField(max_length=50, blank=True)
    plan_opted = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name_plural = "Users"

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this user.
        """
        pass

    def __str__(self):
        return f"{self.email}--{self.uid}"
