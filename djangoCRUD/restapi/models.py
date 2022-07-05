from django.db import models

# Create your models here.


class Employee(models.Model):
    
    empid = models.CharField(max_length=3)
    dob = models.CharField(max_length=15)