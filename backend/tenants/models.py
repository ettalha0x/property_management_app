from django.db import models

# Create your models here.
from django.db import models
from properties.models import Property

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    section_occupied = models.CharField(max_length=255)

    def __str__(self):
        return self.name