# core/views.py
'''
from django.shortcuts import render
from .models import Order
from django.core.mail import send_mail
from django.http import HttpResponse

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        product = request.POST.get('product')
        payment = request.POST.get('payment')

        new_order = Order(
            name=name,
            phone=phone,
            email=email,
            address=address,
            product=product,
            payment=payment,
        )
        new_order.save()

        # Send confirmation to customer
        if email:
            send_mail(
                'Your Order from SHIV Organic Dairy Farm',
                f'Hello {name},\n\nThank you for your order! Your order ID is {new_order.order_id}.',
                'bhosale.shourya255@gmail.com',
                [email],
                fail_silently=False,
            )

        # Send copy to company
        send_mail(
            'New Order Received',
            f'New order placed:\n\nName: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}\nProduct: {product}\nPayment: {payment}',
            'bhosale.shourya255@gmail.com',
            ['bhosale.shourya255@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'orders.html', {'order': Order})

    return HttpResponse("Invalid request", status=400)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Make sure index.html exists
'''
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Order

def index(request):
    return render(request, 'index.html')

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        flat_no = request.POST.get('flat_no')
        town = request.POST.get('town')
        city = request.POST.get('city')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        product = request.POST.get('product')
        payment = request.POST.get('payment')

        new_order = Order(
            name=name,
            phone=phone,
            email=email,
            address=address,
            flat_no=flat_no,
            town=town,
            city=city,
            product=product,
            payment=payment,
            latitude=latitude if latitude else None,
            longitude=longitude if longitude else None
            
        )
        new_order.save()

        # Send confirmation to customer
        if email:
            send_mail(
                'Your Order from SHIV Organic Dairy Farm',
                f'Hello {name},\n\nThank you for your order! Your order ID is {new_order.order_id}.',
                'bhosale.shourya255@gmail.com',
                [email],
                fail_silently=False,
            )

        # Send copy to company
        send_mail(
            'New Order Received',
            f'New order placed:\n\nName: {name}\nPhone: {phone}\nEmail: {email}\nPayment: {payment}',
            'bhosale.shourya255@gmail.com',
            ['bhosale.shourya255@gmail.com'],
            fail_silently=False,
        )

        # Show the customer a "Thank You" page
        return render(request, 'orders.html', {'order': new_order})

    return HttpResponse("Invalid request", status=400)



