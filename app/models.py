
from django.db import models



# Create your models here.


class Emp_details(models.Model):

    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    EMAIL= models.CharField(max_length=255)
    PHONE_NUMBER= models.CharField(max_length=255)
    HIRE_DATE= models.DateField()
    JOB_ID= models.CharField(max_length=255)
    SALARY= models.IntegerField()
    MANAGER_ID= models.IntegerField()
    DEPARTMENT_ID= models.IntegerField()

    def __str__(self):
        return self.FIRST_NAME




class movies(models.Model):

    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100) 
    hero = models.CharField(max_length = 100)
    villian = models.CharField(max_length=100)

    def __str__(self):
        return self.name