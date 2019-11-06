from django.db import models

# Create your models here.

class AcProducts(models.Model):
    name = models.CharField(max_length=64)
    description = models.IntegerField(default=0)
    list_price = models.IntegerField(default=0)
    
    tenant_id = models.ForeignKey(AcTenant, on_delete=models.CASCADE, blank=True, null=True)