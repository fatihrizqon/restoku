from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : "RestoKu - Contact"
    }
    return render(request, 'contact/index.html', context)