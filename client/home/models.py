# client/home/models.py
from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile_no = models.BigIntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
