from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(default=0)
    emp_firstname = models.CharField(max_length=50)
    emp_lastname = models.CharField(max_length=50)
    emp_salary = models.FloatField()
    emp_doj = models.DateTimeField()
    emp_email = models.EmailField(max_length=255)
    emp_phoneno = models.CharField(max_length=10, blank=True)