from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order, OrderItem

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += qty
        else:
            cart_item.quantity = qty
        cart_item.save()
    return redirect('cart')

def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        new_qty = int(request.POST.get('quantity', 1))
        if new_qty > 0:
            item.quantity = new_qty
            item.save()
        else:
            item.delete()
    return redirect('cart')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'checkout.html', {'total': total})

def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        addr = request.POST.get('address')
        cart_items = CartItem.objects.all()
        total = sum(item.total_price() for item in cart_items)

        order = Order.objects.create(full_name=name, phone=phone, address=addr, total_amount=total)
        for item in cart_items:
            OrderItem.objects.create(
                order=order, 
                product_name=item.product.name, 
                quantity=item.quantity, 
                price=item.product.price
            )
        
        cart_items.delete()
        return render(request, 'success.html')
    return redirect('home')