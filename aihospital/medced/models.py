from django.db import models

# Models import
from doctor.models import Profile
# Create your models here.


class Ced(models.Model):
    """"Medical IDs model"""
    cedMed = models.CharField(primary_key=True, db_column="ID", db_index=True, required=True, blank=False)
    doctorProfile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.cedMed
