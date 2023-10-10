from django.shortcuts import render
from django.http import Http404
from inventory.models import Item

def base(request):
    return render(request, 'inventory/base.html')

def index(request):
    items_in_stock = Item.objects.filter(in_stock=True)
    items_not_in_stock = Item.objects.filter(in_stock=False)
    context = {
        'items_in_stock': items_in_stock,
        'items_not_in_stock': items_not_in_stock,
    }
    return render(request, 'inventory/index.html', context)

def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        print(f"Item with id={id} does not exist. Raising Http404.")
        raise Http404('This page does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
