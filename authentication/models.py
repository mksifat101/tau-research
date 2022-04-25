from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from sector.models import Sector


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError('User Must Have A Email Address')

        if not username:
            raise ValueError('User Must Have A Username')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_org = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    obj = MyUserManager()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


class Sadmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)


class Org(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    org_name = models.CharField(max_length=225)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    p_token = models.CharField(max_length=150, null=True)
    create_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.org_name


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    org = models.ForeignKey(
        Org, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    crop_types = models.CharField(max_length=255)
    irrigation = models.CharField(max_length=255)
    p_token = models.CharField(max_length=150, null=True)
    create_date = models.DateTimeField(
        auto_now_add=True, null=True)
