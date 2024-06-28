from django.urls import path
from . import views
urlpatterns = [
    path('productdetails/<int:id>',views.product_details, name = 'productdetails')
]