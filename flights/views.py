from django.utils import timezone
from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer,BookingListSerializer

class flights_List(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class bookings_List(ListAPIView):
    now = timezone.now()
    queryset = Booking.objects.filter(date__gte=now)
    serializer_class = BookingListSerializer