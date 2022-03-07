from django.shortcuts import render, get_object_or_404

from .models import Product

def product(request):

    return render(request, 'product/product.html', {'product': product})