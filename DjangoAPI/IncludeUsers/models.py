from django.db import models

# Create your models here.

class Departaments(models.Model):
    Departaments =  models.AutoField(primary_key=True)
    DepartamentsName = models.CharField(max_length=500)

class Employees(models.Model):
    Employees = models.AutoField(primary_key=True)
    Employees = models.CharField(max_length=500)
    Departaments = models.DateField()
    PhotoFileName = models.CharField(max_length=500)