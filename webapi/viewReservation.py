from rest_framework import generics
from webapi.models import Reservation
from .serializerReservation import ReservationSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class ReservationAPIViewList(generics.ListAPIView):
	lookup_field = 'reservation_id'
	serializer_class = ReservationSerializers
	queryset     = Reservation.objects.all()  

class ReservationAPIView(generics.CreateAPIView):
	lookup_field = 'reservation_id'
	serializer_class = ReservationSerializers
	queryset     = Reservation.objects.all()  

def get_queryset(self):
    return Reservation.objects.all()

def perform_create(self, serializer):
	serializer.save(reservation=self.request.salle)	

class ReservationRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'reservation_id'
	serializer_class = ReservationSerializers
	queryset     = Reservation.objects.all()  

def get_queryset(self):
    return Reservation.objects.all()