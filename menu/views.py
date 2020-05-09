from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
import re
from .forms import Search
from django.db.models import Q

# Method index buat manggil semua data di database dan nampilin ke halaman utama
def index(request):
    data     = Menu.objects.all() # Query buat manggil semua data, karena ada kata kunci all(). Terus variabel data kan berisi SEMUA data yang kita panggil, variabel data kita masukin lagi ke variabel context
    category = Menu.objects.values('category','catslug').distinct() # Buat manggil kategori biar bisa jadi tombol filter
    context  = {
        'title': "RestoKu - Menu", # Judul halaman
        'data' : data, # Data dimasukin sini biar bisa dipanggil di file htmlnya
        'category' : category
    }
    return render(request, 'index.html', context)

# Method category kayak yang udah dijelasin di file urls.py tadi, fungsinya buat ngefilter.
# Ingat di kode (?P<keyword>[\w-]+) ada kata kunci "keyword", keyword ini bisa dikatakan buat nyimpen kata kunci pencarian/filter kita
# Terus keyword tadi kita jadikan parameter di method category biar keywordnya bisa dipake.
def category(request,keyword):
    keyword = re.sub('-+', ' ', keyword) # Skip. Fungsi khusus, bingung jelasinnya wkwk
    # kode di bawah ini sama kayak di atas, yaitu buat manggil. Tapi di sini ada filter, nah fungsi filter ini buat menyaring data yang mau kita cari.
    # di database ada kolom category, nah di filter ini kita nyari data di kolom category pakai kata kunci keyword kita tadi.
    data = Menu.objects.filter(category = keyword)
    # sama kayak penjelasan di atas
    context = {
        'title': "RestoKu - Menu",
        'data' : data,
    }
    return render(request, 'index.html', context)

# Working with limitations
# def search(request):
#     query    = request.GET.get('q')
#     data     = Menu.objects.filter(
#                 Q(name__contains=query) | Q(description__contains=query) | Q(price__contains=query)
#                )
#     context  = {
#         'title'  : "RestoKu - Menu",
#         'result' : data,
#     }
#     return render(request, 'index.html', context)