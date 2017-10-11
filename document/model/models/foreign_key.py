from django.db import models


class Manufacturer(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.car_name}'


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
