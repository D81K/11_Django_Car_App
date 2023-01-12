from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    GEAR = (
        ('a', 'Automatic'),
        ('m', 'Manuel')
    )
    plate_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.SmallIntegerField()
    gaer = models.CharField(max_length=1, choices=GEAR)
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ('id',)


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.customer) + "- " + str(self.car)

    # https://docs.djangoproject.com/en/4.1/ref/models/constraints/#uniqueconstraint
    # UniqueConstraint
    # Creates a unique constraint in the database.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "start_date", "end_date"], name="user_rent_dates"),
        ]