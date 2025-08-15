from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone', 'product__name')
#    list_filter = ('created_at', 'product')
