from django.conf import settings
from django.db import models
from django.utils import timezone


class Module(models.Model):
    registrant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    smiles = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.name