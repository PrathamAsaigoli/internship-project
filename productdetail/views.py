from django.shortcuts import render
from index import models
# Create your views here.
def product_details(request,id):
    single_grocery  = models.Products.objects.get(id=id)
    data = {
        'ProductData': single_grocery
    }
    return render(request,"productdetail.html",data)