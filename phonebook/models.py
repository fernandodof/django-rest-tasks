from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))	
    birthdate = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)