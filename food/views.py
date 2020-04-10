from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def item(request):
    item_details = Item.objects.all()
    # print(item_details)
    context = {
        'item_list':item_details,
    }
    return render(request,'food/index.html',context)

def detail_view(request,item_id):
    result = Item.objects.get(pk = item_id)
    context = {
        'result' :result
    }
    return render(request, 'food/item_detail.html'  ,context)
    # return HttpResponse(f"This is item id : {result}")
    # return HttpResponse("This is item id : %s"% item_id)
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/food/index.html')
    return render(request,'food/item-form.html', {'form':form})
def update_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return redirect('/food/item')
    return render(request, 'food/item-form.html',{'form':form,'item':item})

def delete_item(request, id):
    item = Item.objects.get(id =id)
    if request.method == 'POST':
        item.delete()
        return redirect('/food/item/')
    return render(request, 'food/item-delete.html',{'item' :item})

