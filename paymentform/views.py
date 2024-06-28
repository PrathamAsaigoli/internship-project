from django.shortcuts import render
from addtocart import models
# Create your views here.
def paymentform(request):
        grandtotal = 0.0
        items = models.Addtocart.objects.all()
        for data in items:
            grandtotal += float(data.totalprice)

        data = {
            
            'Allitems' : items,
            'GrandTotal':grandtotal
        
        }  
        return render(request,'paymentform.html',data)

