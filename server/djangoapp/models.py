from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        default=2023
    )
    mileage = models.IntegerField()

    def __str__(self):
        return self.name
