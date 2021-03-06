from django.contrib.auth.models import User
from django.db import models

""""Doctor model, this model controls almost anything"""


# noinspection PyUnresolvedReferences
class Profile(models.Model):
    """"Profile model extends from User, this is a proxy model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=30, blank=True)
    specialty = models.CharField(max_length=60, blank=True)
    bDay = models.DateField(auto_now=False, auto_now_add=False)
    cedMed = models.CharField(unique=True, db_column="Medical ID", db_index=True, blank=False, max_length=30)
    specialtyCed = models.CharField(max_length=20, blank=False, db_column="Specialty ID", db_index=True)

    def __str__(self):
        return f'{self.user.username}, {self.user.first_name}'
