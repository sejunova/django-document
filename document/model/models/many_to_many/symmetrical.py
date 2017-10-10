from django.db import models

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name