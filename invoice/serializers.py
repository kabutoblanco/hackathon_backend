from rest_framework import serializers

from .models import *


class AcTenant(models.Model):
    class Meta:
        model = AcTenant
        fields = ("name")


class AcInvoicesItems(models.Model):
    class Meta:
        model = AcInvoicesItems
        fields = ("quantity", "unit_value", "item_value")


class AcInvoices(models.Model):
    class Meta:
        model = AcInvoices
        fields = ("doc_date", "doc_number", "total_discount",
                  "total_tax", "total_value")
