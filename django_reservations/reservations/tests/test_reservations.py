import pytest
from django_reservations.reservations.models import Rental, Reservation
import datetime
from django_reservations.reservations.views import prepare_table_data


@pytest.mark.django_db
class TestReservationDisplay:
    @classmethod
    def setup_method(cls):
        Rental(rental_name="rental-1").save()
        Rental(rental_name="rental-2").save()

        rental1 = Rental.objects.get(rental_name="rental-1")
        rental2 = Rental.objects.get(rental_name="rental-2")

        Reservation(check_in=datetime.datetime(2022, 1, 1), check_out=datetime.datetime(2022, 1, 13), rental=rental1).save()
        Reservation(check_in=datetime.datetime(2022, 1, 20), check_out=datetime.datetime(2022, 2, 10), rental=rental1).save()
        Reservation(check_in=datetime.datetime(2022, 2, 20), check_out=datetime.datetime(2022, 3, 10), rental=rental1).save()

        Reservation(check_in=datetime.datetime(2022, 1, 2), check_out=datetime.datetime(2022, 1, 20), rental=rental2).save()
        Reservation(check_in=datetime.datetime(2022, 1, 20), check_out=datetime.datetime(2022, 2, 11), rental=rental2).save()
        Reservation(check_in=datetime.datetime(2022, 1, 22), check_out=datetime.datetime(2022, 2, 25), rental=rental2).save()
        Reservation(check_in=datetime.datetime(2022, 1, 25), check_out=datetime.datetime(2022, 2, 26), rental=rental2).save()
        Reservation(id=25, check_in=datetime.datetime(2022, 2, 26), check_out=datetime.datetime(2022, 2, 28), rental=rental2).save()
        Reservation(id=26, check_in=datetime.datetime(2022, 2, 28), check_out=datetime.datetime(2022, 3, 28), rental=rental2).save()

    def test_reservations(self):
        reservation_data = prepare_table_data()
        assert reservation_data[0] == ['rental-1', 1, datetime.date(2022, 1, 1), datetime.date(2022, 1, 13), '-']
        assert reservation_data[1] == ['rental-1', 2, datetime.date(2022, 1, 20), datetime.date(2022, 2, 10), 1]
        assert reservation_data[2] == ['rental-1', 3, datetime.date(2022, 2, 20), datetime.date(2022, 3, 10), 2]

        assert reservation_data[3] == ['rental-2', 4, datetime.date(2022, 1, 2), datetime.date(2022, 1, 20), '-']
        assert reservation_data[4] == ['rental-2', 5, datetime.date(2022, 1, 20), datetime.date(2022, 2, 11), 4]
        assert reservation_data[7] == ['rental-2', 25, datetime.date(2022, 2, 26), datetime.date(2022, 2, 28), 7]
        assert reservation_data[8] == ['rental-2', 26, datetime.date(2022, 2, 28), datetime.date(2022, 3, 28), 25]
