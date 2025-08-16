'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('orders/', views.orders, name='orders'), 
]
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('submit_order/', views.submit_order, name='submit_order'),

]

