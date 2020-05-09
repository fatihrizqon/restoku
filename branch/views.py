from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Branch

# Create your views here.
def index(request):
    data = Branch.objects.all().order_by('-city')
    city = Branch.objects.values('city').distinct()
    context = {
        'title': "RestoKu - Branch",
        'data' : data,
        'city' : city
    }
    return render(request, 'branch/index.html', context)
