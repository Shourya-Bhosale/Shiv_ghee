"""
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
    ('ordered', 'Ordered'),
    ('confirmed', 'Order Confirmed'),
    ('preparing', 'Preparing'),
    ('on_the_way', 'On the Way'),
    ('delivered', 'Delivered'),
]


    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    payment = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"
"""
