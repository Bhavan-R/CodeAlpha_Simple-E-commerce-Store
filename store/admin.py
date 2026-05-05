from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    # 'get_products' thaan andha puthu column
    list_display = ('id', 'full_name', 'get_products', 'total_amount', 'created_at')
    
    def get_products(self, obj):
        return ", ".join([item.product_name for item in obj.items.all()])
    
    get_products.short_description = 'Products Ordered'

admin.site.register(Product)
admin.site.register(CartItem)