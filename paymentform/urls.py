from django.urls import path
from . import views
urlpatterns = [

    path('paymentform',views.paymentform,name='paymentform')
]