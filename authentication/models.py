from django.db import models
from django.contrib.auth.models import AbstractUser
from sector.models import Sector


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_org = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Org(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    org_name = models.CharField(max_length=225)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    p_token = models.CharField(max_length=150, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    p_token = models.CharField(max_length=150, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
