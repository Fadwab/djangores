from rest_framework import generics
from webapi.models import User
from webapi.serializers.UserSerializer import UserSerializers


class UserList(generics.RetrieveUpdateDestroyAPIView):
	pass
	lookup_field = 'matricule'
    serializer_class = UserSerializers
   # queryset     = User.objects.all()  

    def get_queryset(self):
        return User.objects.all()

    #def get_object(self):
       # pass User.objects.all()  
		