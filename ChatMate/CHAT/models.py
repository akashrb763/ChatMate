from django.db import models

# Create your models here.
class Finder(models.Model):
    f_name=models.CharField(max_length=18)
    l_name=models.CharField(max_length=18)
    birthdate=models.DateField()
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)



class Register(models.Model):
    f_name=models.CharField(max_length=18)
    l_name=models.CharField(max_length=18)
    birthdate=models.DateField()
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    u_name=models.CharField(max_length=25)
    link=models.CharField(max_length=50)