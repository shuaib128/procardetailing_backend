from datetime import date
from django.db import models
from djmoney.models.fields import MoneyField

# Restriced Areas
class Area(models.Model):
    name = models.CharField(max_length=1000, default="name")
    zipcode = models.IntegerField(default=98208)

    def __str__(self):
        return f"{self.name}-{self.zipcode}"



class Appointment(models.Model):
    date = models.CharField(max_length=1000, default="date")

    def __str__(self):
        return self.date