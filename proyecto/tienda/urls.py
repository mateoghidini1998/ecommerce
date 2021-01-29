from django.urls import path
from . import views

urlpatterns = [

    path('', views.tienda, name="tienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
]