from django.shortcuts import render, redirect
from .models import Product


def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapp/index.html', context)


def indexitem(request, my_id):
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


def update_item(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.descriptions = request.POST.get('descriptions')
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect('/myapp/')
    context = {
        'item': item
    }
    return render(request, 'myapp/updateitem.html', context)
