from django.contrib import admin
from .models import User 
from .models import Reservation
from .models import Salle

admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Salle)
# Register your models here.
