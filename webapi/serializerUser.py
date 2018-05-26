from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import(
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    )


User = get_user_model()
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            'matricule',
            
            'username',
            'password', 
            'email' ,
            'nom',
            'role'
            
            
             
            ]

#class UserCreateSerializer(ModelSerializer):
#   email = serializers.EmailField(label='Email adress')
#    email2 = serializers.EmailField(label='Confirm Email')
 #   class Meta:
  #      model = User
   #     fields = [
    #        'username',
            
            
     #       'password',
      #      'email2',
       #     'email',
        #    'matricule',
         #   'nom'
            
            
        #]
        #extra_kwargs = {"password":
         #                   {"write_only":True}
          #                }
    #def validate(self, data):
     #   email = data['email']
      #  user_qs = User.objects.filter(email=email)  
       # if user_qs.exists():
        #   raise ValidationError("This user has already registered.")
        #return data                
    #def validate_email(self, value):
    #   data = self.get_initial()
    #    email1 = data.get("email2")
     #   email2 = value
      #  if email1 != email2:
       #     raise ValidationError("Emails must match.")

        #return value                      
    #def validate_email2(self, value):
     #   data = self.get_initial()
      #  email1 = data.get("email")
       # email2 = value
        #if email1 != email2:
         #   raise ValidationError("Emails must match.")
        #return value

    #def create(self, validated_data):
     #   username = validated_data['username']

      #  email = validated_data['email']
      #  password = validated_data['password']
       # user_obj = User(
        #       username = username,
              
          #     email =email
          #  ) 
        #user_obj.set_password(password)
       # user_obj.save()
        #return validated_data








class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True , read_only=True)
    #username = CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email adress',required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = [
            #'username',
            'password',
            
            'email',
            
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                          }
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password",None)
        password = data["password"]
        if not email and not password:
            raise ValidationError("A oassword or email is required to login")
        user = User.objects.filter(
                Q(email=email) |
                Q(password=password)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj=user.first()
        else:
            raise ValidationError("This password/email is not valid")
        ##if user_obj:
          ##  if not user_obj.check_password(password):
            ##    raise ValidationError("INCORRECT credentials pelease try again")
            data["token"] = "SOME RANDOM TOKEN"     
        return data
        #email = data['email']
        #user_qs = User.objects.filter(email=email) 
        #if user_qs.exists():
         #  raise ValidationError("This user has already registered.")
