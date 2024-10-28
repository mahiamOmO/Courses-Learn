from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}  # Wrap the QuerySet in a dictionary
    return render(request, 'index.html', context)


def new(request):
    return HttpResponse('New Products')