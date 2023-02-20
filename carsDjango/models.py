import datetime
from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=200)
    carModel = models.CharField(max_length=200)
    yearOfConstruct = models.DateField()
    cylindre = models.IntegerField(default=0)
    version = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}, {self.brand}, {self.carModel}, {self.yearOfConstruct}, {self.cylindre}, {self.version}'
