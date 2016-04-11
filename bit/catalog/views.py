from django.shortcuts import render_to_response
from django.http import Http404
from .models import *

def index(request):
    categories = Category.objects.all()
    return render_to_response('catalog/index.html', {'categories': categories})

def category_product(request, id_category):
    try:
        category = Category.objects.get(id=id_category)
    except Category.DoesNotExist:
        raise Http404('Not category')

    products = Product.objects.filter(product_category=id_category)
    return render_to_response('catalog/category.html', {'products': products})