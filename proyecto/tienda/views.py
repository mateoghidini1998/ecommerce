from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.

def tienda(request):
    products = Product.objects.all()
    context = {'products':products}

    return render(request, 'tienda/tienda.html', context)

def carrito(request):
    
    if request.user.is_authenticated: #Si el usuario esta logeado

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #Obtiene un objeto si existe y sino lo crea
        items = order.orderitem_set.all()
    
    else: #Si el usuario no esta logeado
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items, 'order':order}

    return render(request, 'tienda/carrito.html', context)

def checkout(request):
    
    if request.user.is_authenticated: #Si el usuario esta logeado

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #Obtiene un objeto si existe y sino lo crea
        items = order.orderitem_set.all()
    
    else: #Si el usuario no esta logeado
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items, 'order':order}

    

    return render(request, 'tienda/checkout.html', context)

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('producdtId:', productId)
    return JsonResponse('El item fue agregado', safe=False)