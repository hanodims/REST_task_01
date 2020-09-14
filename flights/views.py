from datetime import datetime
from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer,BookingListSerializer

class flights_List(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class bookings_List(ListAPIView):
    #now = datetime.today()
    queryset = Booking.objects.all()#need to add query date > now
    serializer_class = BookingListSerializer