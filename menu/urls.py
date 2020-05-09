from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = [
    # Sama kayak di urls.py webku tadi, di App Menu ada juga index. Sesuai kebutuhan sih pakai atau enggak. Tapi sebagai default dipakai gapapa.
    # Jadi kalau di Webku tadi ada kode [    url(r'^menu/', include('menu.urls')),    ] fungsinya adalah ketika kita nulis di address bar browser kayak gini localhost:8000/menu, maka nanti manggil kode di bawah ini.
    # Karena di Route utama (urls.py di webku) kita nulis [    url(r'^menu/', include('menu.urls')),    ], secara otomatis kode di bawah ini dipanggil
    # Arti kode di bawah ini = memanggil method index di dalam file views.py folder Menu
    url(r'^$', views.index),
    # Kode di bawah ini masuk fungsi filter
    # (?P<keyword>[\w-]+) aku bingung jelasinnya, fungsinya pokoknya buat masukin keyword/kata kunci buat filter yang nanti akan dilempar ke method category di file views.py
    # Sekarang buka file views di folder Menu
    url(r'^(?P<keyword>[\w-]+)/$', views.category),
    
]