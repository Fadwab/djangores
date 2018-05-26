from rest_framework import serializers

from .models import Salle
 
class SalleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = [ 
            'salle_id',
            'nom',
            'etage', 
            'capacite' , 
            'bloc' ,
            'vedeo_conf', 
            'retroprojecteur',
            'tableau',
            'climatisation']