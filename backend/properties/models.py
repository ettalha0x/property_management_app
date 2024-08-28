from django.db import models

# Create your models here.
from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
    ]
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    number_of_units = models.IntegerField()
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name