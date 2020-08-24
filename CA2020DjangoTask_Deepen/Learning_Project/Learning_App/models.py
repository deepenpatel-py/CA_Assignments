from django.db import models

# Create your models here.

class employees(models.Model):
    name=models.CharField(max_length=20)
    id=models.IntegerField(default=0,primary_key=True)
    contact=models.IntegerField(default=0)
    address=models.CharField(max_length=50)

class company(models.Model):
    comp_name=models.CharField(max_length=10)
    phone = models.IntegerField(default=0)
    add = models.CharField(max_length=20)
