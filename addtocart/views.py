from django.shortcuts import render,redirect
from index import models
from . import models as mo


# Create your views here.
def addtocart(request,id):

    if request.method == "POST":
            item = models.Products.objects.get(id=id)
            
            Name = item.name
            Price = item.price
            Quantity = request.POST['quantity']
            Totalprice = float(Quantity)*float(Price)
            Img = item.img

            data = mo.Addtocart(name=Name,price=Price,quantity=Quantity,totalprice=Totalprice,img=Img)
            data.save()
            return redirect('productdetails',id=id) 

    

def cartproducts(request):
        grandtotal = 0.0
        items = mo.Addtocart.objects.all()
        item_count = items.count()
        for data in items:
            grandtotal += float(data.totalprice)

        data = {
            
            'GrandTotal':grandtotal,
            'Allitems' : items,

        
        } 
        
        return render(request,'addtocart.html',data)

def cartcount(request):
    items = mo.Addtocart.objects.all()
    item_count = items.count()

    
    data = {
            'ItemCount':item_count,
        }
    
    return render (request, 'layout.html',data)
      

def deletecartitem(request,id):
      
      cart_item = mo.Addtocart.objects.get(id=id)
      cart_item.delete()

      return redirect('cartproducts')
      