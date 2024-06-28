from django.db import models

# Create your models here.
class Addtocart(models.Model):
    name = models.CharField(max_length=255,)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    totalprice = models.CharField(max_length=255)
    img = models.ImageField(upload_to="cart",max_length=250,null=True,default=None)