from django.urls import path
from . import views
urlpatterns = [
    path('cart/<int:id>',views.addtocart, name="addtocart"),
    path('cartproducts', views.cartproducts, name="cartproducts"),
    path('cartcount', views.cartcount, name="cartcount"),
    path('deletecartitem/<int:id>', views.deletecartitem , name="deletecartitem")
]