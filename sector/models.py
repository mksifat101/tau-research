from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
