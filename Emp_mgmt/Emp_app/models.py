from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Signup(AbstractUser):
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=255)
    
class Employee(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
 

class DynamicField(models.Model):
    field_name = models.CharField(max_length=100,null=True, blank=True)
    field_type = models.CharField(max_length=50,null=True, blank=True, choices=[
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('boolean', 'Boolean')
    ])


class EmployeeFieldValue(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    dynamic_field = models.ForeignKey(DynamicField, on_delete=models.CASCADE,null=True)
    field_value = models.CharField(max_length=255,null=True, blank=True) 


    
    


