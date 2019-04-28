from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item, List

# Create your views here.


def home_page(request):
    # if request.method == "POST":
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/list/the-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # list_ = Item.objects.all().first()
    # print(Item.objects.all())
    # print('list_id', list_id)
    # print('kaka', list_)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/list/%d/' % list_.id)
