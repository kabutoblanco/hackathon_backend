from django.db import models
from customer.models import *

# Create your models here.
from pg_partitioning.decorators import ListPartitioning


class AcTenant(models.Model):
    name = models.CharField(max_length=64)


@ListPartitioning(partition_key="tenant_id")
class AcProducts(models.Model):
    name = models.CharField(max_length=64)
    description = models.IntegerField(default=0)
    list_price = models.FloatField(default=0)

    tenant_id = models.ForeignKey(
        AcTenant, on_delete=models.CASCADE, blank=True, null=True)


class AcInvoicesItems(models.Model):
    quantity = models.FloatField(default=0)
    unit_value = models.FloatField(default=0)
    item_value = models.FloatField(default=0)

    tenant_id = models.ForeignKey(
        AcTenant, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(
        AcProducts, on_delete=models.CASCADE, blank=True, null=True)


class AcInvoices(models.Model):
    doc_date = models.CharField(max_length=64)
    doc_number = models.IntegerField(default=0)
    total_discount = models.IntegerField(default=0)
    total_tax = models.IntegerField(default=0)
    total_value = models.IntegerField(default=0)

    tenant_id = models.ForeignKey(
        AcTenant, on_delete=models.CASCADE, blank=True, null=True)

    # Foreign Keys
    ac_invoice_item_id = models.ForeignKey(
        AcInvoicesItems, on_delete=models.CASCADE, blank=True, null=True)
    tenant_id = models.ForeignKey(
        AcTenant, on_delete=models.CASCADE, blank=True, null=True)
    customer_id = models.ForeignKey(
        Customers, on_delete=models.CASCADE, blank=True, null=True)
