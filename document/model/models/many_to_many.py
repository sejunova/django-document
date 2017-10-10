from django.db import models

__all__ = (
    'Pizza',
    'Topping',
    'TwitterUser',
)


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name