from django.db import models
from django.utils import timezone
from django.conf import settings


class RTG(models.Model):
    file = models.FileField(upload_to='file')
    diagnose = models.BooleanField(null=True)
    date = models.DateTimeField(default=timezone.now)
    # wsparcie dla diagnozy
    support = models.IntegerField(null=True)
    # diagnoza specjalisty
    doctor_diagnose = models.BooleanField(null=True)
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)


class Patient(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    pesel = models.CharField(max_length=11)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name)



