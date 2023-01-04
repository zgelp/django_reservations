from django.db import models
from django.db.models import Subquery, OuterRef


class ReservationManager(models.Manager):
    def with_previous_reservation_id(self):
        return self.all().order_by('rental', 'check_in').annotate(
            previous_reservation_id=Subquery(
                Reservation.objects.filter(
                    rental=OuterRef('rental'), check_in__lt=OuterRef('check_in')
                ).order_by('-check_in').values('id')[:1]
            )
        ).values()


class Rental(models.Model):
    rental_name = models.CharField(max_length=40)


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    objects = ReservationManager()
