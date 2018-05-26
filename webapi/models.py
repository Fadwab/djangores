from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    matricule = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=250)
    role = models.IntegerField(default=1)
   
    

def __str__(self):
    return self.user


class Salle(models.Model):
    salle_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=250)
    etage = models.CharField(max_length=250)
    capacite = models.IntegerField(default=0)
    bloc = models.CharField(max_length=250)
    vedeo_conf = models.BooleanField(default=False)
    retroprojecteur = models.BooleanField(default=False)
    tableau = models.BooleanField(default=False)
    climatisation = models.BooleanField(default=False)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    heure_deb = models.DateTimeField(null=True, blank=True)
    heure_fin = models.DateTimeField(null=True, blank=True) 
    nb_participants = models.IntegerField(default=0)
    statut = models.CharField(max_length=250)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=250)
    file = models.FileField(default="test.txt")


