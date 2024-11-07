from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all()

    return render(request, 'inventory/index.html', {
        'items': items,
    })

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    return render(request, 'inventory/add_item.html', {
        'form': form,
    })