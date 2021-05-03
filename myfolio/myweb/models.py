from django.db import models
import datetime
# Create your models here.

class Resume:
	name : str
	des : str
	img : str

class User(models.Model):
    
    First_Name = models.CharField(max_length=240)
    Last_Name = models.CharField(max_length=240)
    Email = models.EmailField(max_length=240)
    Phone = models.CharField(max_length=12 ,default=True)
    message = models.TextField(default=True)
    date = models.DateField()
    
    def __str__(self):
        return self.First_Name
    