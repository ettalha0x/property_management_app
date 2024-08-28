from django.db import models

# Create your models here.
from django.db import models
from tenants.models import Tenant

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    settled = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment by {self.tenant.name} on {self.date_paid}"