from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name

class Register(models.Model):
    gender = (("Female","Female"),("Male","Male"),("Other","Other"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, choices=gender, default="Female")
    Phone_Number = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + self.user.last_name