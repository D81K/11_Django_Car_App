from django.db import models


# Create your models here.

class Car(models.Model):
    plate_number = models.CharField(max_length=30, unique=True)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.SmallIntegerField()
    rent_per_day = models.IntegerField()
    available = models.BooleanField(default=True)

    GEAR = (
        ('a', 'Automatic'),
        ('m', 'Manuel')
    )
    gear = models.CharField(max_length=1, choices=GEAR, null=True)

    def __str__(self):
        return self.brand + ' ' + self.model


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.car     # Add customer
