from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapp/index.html', context)

def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request, 'myapp/detail.html', context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        descriptions = request.POST.get('descriptions')
        image = request.FILES['upload']
        item = Product(name=name, price=price, descriptions=descriptions, image=image)
        item.save()
    return render(request, 'myapp/additem.html')


