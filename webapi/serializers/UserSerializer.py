from rest_framework import serializers

from webapi.models import User
 
 class UserSerializers(serializers.ModelSerializer):
     class Meta:
        model = User
         fields = [ 'matricule','nom','prenom', 'email' , 'email' , 'adresse', 'mot_de_passe' ]
         
	
	
	
	