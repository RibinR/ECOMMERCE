from . import views
from django.urls import path
app_name='cart'
urlpatterns=[
path("add/<int:pro_id>/",views.add_cart,name="add_cart"),
path('',views.cart_detail,name='cart_detail'),
path("minus/<int:pro_id>/",views.cart_minus,name="minus"),
path("delete/<int:pro_id>/",views.dlt,name="delete")

]