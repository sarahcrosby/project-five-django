from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """
    Lists all products
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def product_detail(request, pk):
    """
    Creates a page with full product details
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})