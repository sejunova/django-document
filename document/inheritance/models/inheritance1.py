from django.db import models

__all__=(
    'School',
    'CommonInfo',
    'Student',
    'Teacher',
)

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,
                               blank=True,
                               null=True,
                               related_name="%(app_label)s_%(class)s_related",
                               )
    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name

