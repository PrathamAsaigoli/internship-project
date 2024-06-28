from django.db import models
from django.conf import settings

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img = models.ImageField(upload_to="media",max_length=250,null=True,default=None)
    decription = models.CharField(max_length=255,default=None)