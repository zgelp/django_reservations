from django.core.management.base import BaseCommand
from django_reservations.reservations.models import Rental, Reservation
import datetime


class Command(BaseCommand):
    help = 'Seeds database with data from example file'

    def handle(self, *args, **options):
        Rental(rental_name="rental").save()
        Rental(rental_name="rental").save()

        rental1 = Rental.objects.get(id=1)
        rental2 = Rental.objects.get(id=2)

        Reservation(check_in=datetime.datetime(2022, 1, 1), check_out=datetime.datetime(2022, 1, 13),
                    rental=rental1).save()
        Reservation(check_in=datetime.datetime(2022, 1, 20), check_out=datetime.datetime(2022, 2, 10),
                    rental=rental1).save()
        Reservation(check_in=datetime.datetime(2022, 2, 20), check_out=datetime.datetime(2022, 3, 10),
                    rental=rental1).save()

        Reservation(check_in=datetime.datetime(2022, 1, 2), check_out=datetime.datetime(2022, 1, 20),
                    rental=rental2).save()
        Reservation(check_in=datetime.datetime(2022, 1, 20), check_out=datetime.datetime(2022, 2, 11),
                    rental=rental2).save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
