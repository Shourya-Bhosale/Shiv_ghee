# core/models.py
'''
import uuid
from django.db import models
#from django.utils import timezone

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    product = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='order Confirmed')
#    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.order_id}"
    
from django.db import models
import uuid

class Order(models.Model):
    order_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="0000000000")
    email = models.EmailField()
    address= models.TextField(null=True, blank=True)  # Full address
    flat_no = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, default="Unknown Product")
#    flat_no = models.CharField(max_length=255, blank=True, null=True)
#    town = models.CharField(max_length=255, blank=True, null=True)
#    city = models.CharField(max_length=255, blank=True, null=True)
    payment = models.CharField(max_length=50, default="Pending")
#    product = models.CharField(max_length=100) 
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')    # ✅ Add this
    created_at = models.DateTimeField(auto_now_add=True)
    instruction = models.TextField(null=True, blank=True)  # Delivery instructions
    

    def __str__(self):
        return f"Order {self.order_id} by {self.name}"
     '''

# core/models.py

from django.db import models
import uuid

class Order(models.Model):
    order_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=100, blank=True, null=True)
    flat_no = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    payment = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # Order status

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())[:8]  # Short unique ID
        super().save(*args, **kwargs)

