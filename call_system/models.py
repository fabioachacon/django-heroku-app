from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    room = models.IntegerField()

    def __str__(self):
        return self.name