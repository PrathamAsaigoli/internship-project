from django.db import models

# Create your models here.
class Signup(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
  
class Login(models.Model):

    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)





