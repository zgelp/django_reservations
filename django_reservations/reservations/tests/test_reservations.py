import pytest
from django_reservations.reservations.models import Rental, Reservation
import datetime
from django_reservations.reservations.views import reservations_with_previous_reservation_id


@pytest.mark.django_db
class TestReservationDisplay:
    @classmethod
    def setup_method(cls):
        Rental(rental_name="rental").save()
        Rental(rental_name="rental").save()

        rental1 = Rental.objects.get(id=1)
        rental2 = Rental.objects.get(id=2)

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
        reservation_data = reservations_with_previous_reservation_id()
        assert reservation_data[0] == {'id': 1, 'rental_id': 1, 'check_in': datetime.date(2022, 1, 1), 'check_out': datetime.date(2022, 1, 13), 'previous_reservation_id': None}
        assert reservation_data[1] == {'id': 2, 'rental_id': 1, 'check_in': datetime.date(2022, 1, 20), 'check_out': datetime.date(2022, 2, 10), 'previous_reservation_id': 1}
        assert reservation_data[2] == {'id': 3, 'rental_id': 1, 'check_in': datetime.date(2022, 2, 20), 'check_out': datetime.date(2022, 3, 10), 'previous_reservation_id': 2}

        assert reservation_data[3] == {'id': 4, 'rental_id': 2, 'check_in': datetime.date(2022, 1, 2), 'check_out': datetime.date(2022, 1, 20), 'previous_reservation_id': None}
        assert reservation_data[4] == {'id': 5, 'rental_id': 2, 'check_in': datetime.date(2022, 1, 20), 'check_out': datetime.date(2022, 2, 11), 'previous_reservation_id': 4}
        assert reservation_data[7] == {'id': 25, 'rental_id': 2, 'check_in': datetime.date(2022, 2, 26), 'check_out': datetime.date(2022, 2, 28), 'previous_reservation_id': 7}
        assert reservation_data[8] == {'id': 26, 'rental_id': 2, 'check_in': datetime.date(2022, 2, 28), 'check_out': datetime.date(2022, 3, 28), 'previous_reservation_id': 25}
