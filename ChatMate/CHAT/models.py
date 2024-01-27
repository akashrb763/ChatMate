from django.db import models

# Create your models here.
class Finder(models.Model):
    f_name=models.CharField(max_length=18,blank=True,null=True)
    l_name=models.CharField(max_length=18,blank=True,null=True)
    birthdate=models.DateField()
    email=models.CharField(max_length=25,blank=True,null=True)
    phone=models.CharField(max_length=12,blank=True,null=True)
    gender=models.CharField(max_length=7,blank=True,null=True)



class Register(models.Model):
    f_name=models.CharField(max_length=18,blank=True,null=True)
    l_name=models.CharField(max_length=18,blank=True,null=True)
    birthdate=models.DateField()
    email=models.CharField(max_length=25,blank=True,null=True)
    phone=models.CharField(max_length=12,blank=True,null=True)
    u_name=models.CharField(max_length=25,blank=True,null=True)
    link=models.CharField(max_length=50,blank=True,null=True)
    other=models.CharField(max_length=400,blank=True,null=True)
    gender=models.CharField(max_length=7,blank=True,null=True)


class Details(models.Model):
    f_f_name=models.CharField(max_length=18,blank=True,null=True)
    f_l_name=models.CharField(max_length=18,blank=True,null=True)
    f_birthdate=models.DateField()
    f_email=models.CharField(max_length=25,blank=True,null=True)
    f_phone=models.CharField(max_length=12,blank=True,null=True)
    f_gender=models.CharField(max_length=7,blank=True,null=True)

    mate_f_name=models.CharField(max_length=18,blank=True,null=True)
    mate_l_name=models.CharField(max_length=18,blank=True,null=True)
    mate_birthdate=models.DateField()
    mate_email=models.CharField(max_length=25,blank=True,null=True)
    mate_phone=models.CharField(max_length=12,blank=True,null=True)
    mate_u_name=models.CharField(max_length=25,blank=True,null=True)
    mate_link=models.CharField(max_length=50,blank=True,null=True)
    mate_other=models.CharField(max_length=400,blank=True,null=True)
    meta_gender=models.CharField(max_length=7,blank=True,null=True)

  
