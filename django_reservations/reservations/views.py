from django.shortcuts import render
from django_reservations.reservations.models import Rental


def prepare_table_data():
    rentals = Rental.objects.all()
    record_id = 0
    prepared_data = []
    for rental in rentals:
        previous_rental_id = 0
        for reservation in rental.reservation_set.all().order_by("check_in"):
            last_id = reservation.id - 1 if previous_rental_id != 0 else "-"
            prepared_data.append([rental.rental_name, reservation.id, reservation.check_in, reservation.check_out, last_id])
            previous_rental_id += 1
            record_id += 1
    return prepared_data


def reservations_view(request):
    rentals = prepare_table_data()
    return render(request, 'reservation_table.html', {'rentals': rentals})
