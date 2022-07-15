from . import views
from django.urls import path
app_name='shop'
urlpatterns=[
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='pbc'),
    path('<slug:c_slug>/<slug:p_slug>/', views.prdtdetail, name='procatdetail'),
    path('/back', views.back, name='back'),
]