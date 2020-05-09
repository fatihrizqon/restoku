from django.shortcuts import render
from menu.models import Menu
from menu.forms import Search
from django.db.models import Q
from django.http import HttpResponse
from functools import reduce
from operator import or_, and_

def index(request):
    data = Menu.objects.all()
    category = Menu.objects.values('category','catslug').distinct()
    context = {
        'title': "RestoKu - Menu",
        'data' : data,
        'category' : category
    }
    return render(request, 'index.html', context)

# Working with limitations
def search(request):
    # query    = request.GET.get('q')
    # data     = Menu.objects.filter(
    #             Q(name__contains=query) | Q(description__contains=query) | Q(price__contains=query)
    #            )
    # context  = {
    #     'title': "RestoKu - Menu",
    #     'data' : data,
    # }
    # return render(request, 'index.html', context)


    data = Menu.objects.filter(query).distinct()
    context  = {
        'title': "RestoKu - Menu",
        'data' : data,
    }
    return render(request, 'index.html', context)