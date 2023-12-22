from django.db import models

class Users(models.Model):
    #username_id = models.IntegerField(primary_key=True)
    username = models.CharField(primary_key=True, max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Vehicle(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    truck_num = models.IntegerField()

# Create your models here.
