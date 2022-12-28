from django.shortcuts import render
from django_reservations.reservations.utils import reservations_with_previous_reservation_id


def reservations_view(request):
    reservations = reservations_with_previous_reservation_id()
    return render(request, 'reservation_table.html', {'reservations': reservations})
