from django.shortcuts import render
from index import models

# Create your views here.
def groceries(request):

    all_grocery  = models.Products.objects.all()
    data = {
        'GroceryData' : all_grocery       
    }

    return render(request,"groceries.html",data)