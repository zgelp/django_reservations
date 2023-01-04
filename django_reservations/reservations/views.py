from django.shortcuts import render
from django_reservations.reservations.models import Reservation


def reservations_view(request):
    reservations = Reservation.objects.with_previous_reservation_id()
    return render(request, 'reservation_table.html', {'reservations': reservations})
