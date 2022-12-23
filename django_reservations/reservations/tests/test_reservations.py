import pytest
from django_reservations.reservations.models import Rental, Reservation
from datetime import datetime
from django_reservations.reservations.views import prepare_table_data

@pytest.mark.django_db
class TestReservationDisplay:
    @classmethod
    def setup_method(cls):
        Rental(rental_name="rental-1").save()
        Rental(rental_name="rental-2").save()

        rental1 = Rental.objects.get(rental_name="rental-1")
        rental2 = Rental.objects.get(rental_name="rental-2")

        Reservation(check_in=datetime(2022, 1, 1), check_out=datetime(2022, 1, 13), rental=rental1).save()
        Reservation(check_in=datetime(2022, 1, 20), check_out=datetime(2022, 2, 10), rental=rental1).save()
        Reservation(check_in=datetime(2022, 2, 20), check_out=datetime(2022, 3, 10), rental=rental1).save()

        Reservation(check_in=datetime(2022, 1, 2), check_out=datetime(2022, 1, 20), rental=rental2).save()
        Reservation(check_in=datetime(2022, 1, 20), check_out=datetime(2022, 2, 11), rental=rental2).save()
        Reservation(check_in=datetime(2022, 1, 22), check_out=datetime(2022, 2, 25), rental=rental2).save()
        Reservation(check_in=datetime(2022, 1, 25), check_out=datetime(2022, 2, 26), rental=rental2).save()

    def test_reservations(self):
        data = prepare_table_data()