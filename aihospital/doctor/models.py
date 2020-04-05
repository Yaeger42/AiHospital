from django.contrib.auth.models import User
from django.db import models
from medced.models import Ced
""""Doctor model, this model controls almost anything"""


class Profile(models.Model):
    """"Profile model extends from User, this is a proxy model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=30, blank=True)
    specialty = models.CharField(max_length=60, blank=True)
    cedID = models.ForeignKey(Ced, max_length=20, on_delete=models.CASCADE, related_name='+',
                              db_column="Medical Id card")
    bday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.name