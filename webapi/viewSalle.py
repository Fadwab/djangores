from rest_framework import generics
from webapi.models import Salle
from .serializerSalle import SalleSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class SalleAPIViewList(generics.ListAPIView):
	lookup_field = 'matricule'
	serializer_class = SalleSerializers
	queryset     = Salle.objects.all()  

class SalleAPIView(generics.CreateAPIView):
	lookup_field = 'salle_id'
	serializer_class = SalleSerializers
	queryset     = Salle.objects.all()  

def get_queryset(self):
    return Salle.objects.all()

def perform_create(self, serializer):
	serializer.save(salle=self.request.salle)





class SalleRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'salle_id'
	serializer_class = SalleSerializers
	queryset     = Salle.objects.all()  

def get_queryset(self):
    return Salle.objects.all()
