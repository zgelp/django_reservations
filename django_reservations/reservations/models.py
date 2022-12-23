from django.db import models


class Rental(models.Model):
    rental_name = models.CharField(max_length=40)


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
