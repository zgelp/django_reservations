from django_reservations.reservations.models import Reservation
from django.db.models import Subquery, OuterRef


def reservations_with_previous_reservation_id():
    all_reservations = Reservation.objects.all().order_by('rental', 'check_in')
    reservations = all_reservations.annotate(
        previous_reservation_id=Subquery(
            Reservation.objects.filter(
                rental=OuterRef('rental'), check_in__lt=OuterRef('check_in')
            ).order_by('-check_in').values('id')[:1]
        )
    )
    return reservations.values()
