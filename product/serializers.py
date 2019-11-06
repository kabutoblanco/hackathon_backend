from rest_framework import serializers

from .models import *


class AcTenant(models.Model):
    class Meta:
        model = AcProducts
        fields = ("name", "description", "list_prices")
