'''
from django.core.mail import send_mail
from .models import Order  # Capital 'O'
from django.shortcuts import render
from django.http import HttpResponse

def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        product = request.POST.get('product')
        payment = request.POST.get('payment')

        if not email:
            print("❌ No email provided in the form. Skipping email sending.")

        order = Order.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            product=product,
            payment=payment
        )

        # 📩 Email to Customer
        if email:
            customer_subject = 'Your Order from SHIV Organic Dairy Farm'
            customer_message = f"""Hello {name},

Thank you for your order! Your order ID is {order.order_id}.

Product: {product}
Status: {order.status}

We will notify you once your order has been dispatched.
"""
            send_mail(
                customer_subject,
                customer_message,
                'bhosale.shourya255@gmail.com',
                [email],
                fail_silently=False
            )
            print("✅ Email sent to customer.")

        # 📩 Email to Company
        company_subject = f"📦 New Order Received: {order.order_id}"
        company_message = f"""
New order received from {name}.

Details:
Name: {name}
Phone: {phone}
Email: {email}
Address: {address}
Product: {product}
Payment: {payment}

Order ID: {order.order_id}
"""
        send_mail(
            company_subject,
            company_message,
            'bhosale.shourya255@gmail.com',  # From
            ['bhosale.shourya255@gmail.com'],  # To company (same or another)
            fail_silently=False
        )
        print("✅ Email sent to company.")

        return render(request, 'order_success.html', {'order': order})
    else:
        return HttpResponse("Invalid Request", status=400)
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

        full_address = f"{flat_no}, {town}, {city}"

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

        if email:
            send_mail(
                'Your Order from SHIV Organic Dairy Farm',
                f'Hello {name},\n\nThank you for your order! Your order ID is {new_order.order_id}.',
                'bhosale.shourya255@gmail.com',
                [email],
                fail_silently=False,
            )

        send_mail(
            'New Order Received',
            f'New order placed:\n\nName: {name}\nPhone: {phone}\nEmail: {email}\nflat_no:{flat_no}\ntown: {town}\ncity:{city}\nPayment: {payment}',
            'bhosale.shourya255@gmail.com',
            ['bhosale.shourya255@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'orders.html', {'order': new_order})

    return HttpResponse("Invalid request", status=400)
