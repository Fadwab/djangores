from rest_framework import serializers

from .models import Reservation
 
class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [ 
            'reservation_id',
            'date',
            'heure_deb', 
            'heure_fin' , 
            'nb_participants' ,
            'statut', 
            'salle',
            'user',
            'titre',
            'file'
            ]