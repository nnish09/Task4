from django.db import models
import re
from django.core.validators import RegexValidator


class Client(models.Model):
    client_name=models.CharField(max_length=60, blank=True,unique=True)
    email=models.EmailField(max_length=100,blank=True)
    contact_name=models.CharField(max_length=60, blank=True)
    street_name=models.TextField()
    suburb=models.TextField(unique=True)
    postcode=models.CharField(max_length=10,null=True,blank=True)
    state=models.CharField(max_length=200, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be upto 10 digits")
    phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    
    def __str__(self):
        return self.client_name