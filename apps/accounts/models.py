from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Agency(models.Model):
    topaz_code = models.CharField(max_length=100,unique=True)
    ebs_code = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=130)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE,related_name="agency_user",blank=True,null=True)
    email = models.EmailField(blank=False,null=False, unique=True)
    dni = models.CharField(max_length=10,unique=True,null=True,blank=True)
    birthdate = models.DateField(auto_created=False, auto_now=False, null=True,blank=True)
    zone = models.CharField(max_length=50,blank=True)
    shoe_size = models.PositiveIntegerField(default=0,blank=True)
    polo_size = models.CharField(max_length=3,blank=True)
    bank = models.CharField(max_length=30,blank=True)
    yaple_plin = models.CharField(max_length=30,blank=True)
    account = models.CharField(max_length=40,blank=True)
    cci = models.CharField(max_length=70,blank=True)
    is_delete = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.username
    
    @property
    def rol(self):
        return self.groups.first()