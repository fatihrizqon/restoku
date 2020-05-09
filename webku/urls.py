from django.conf.urls import url, include  #import include biar bisa memanggil fungsi include
from django.contrib import admin #import bawaan django
from . import views #import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render

urlpatterns = [
    # URL untuk mengakses halaman admin halaman admin fungsinya ya untuk admin.
    url(r'^admin/', admin.site.urls),
    # URL untuk mengakses halaman index/landing page/halaman pertama kali muncul ketika mengakses website.
    # Caranya adalah pertama import dulu views.py "from . import views" soalnya kita pengen bikin method-methodnya di views.py
    # Karena "nggak etis" kita bikin method di route (file urls.py) ini
    url(r'^$', views.index),
    # Nah, URL di bawah ini beda file & folder, maka perlu memanggil fungsi include biar bisa memanggil file/folder di luar folder Webku
    # menu, branch, contact yang udah dibikin ini dalam django disebut App. Sedangkan di awal django kita kan bikin project (startproject) yang namanya "webku"
    # Project bisa diibaratkan sebagai Ketua yang punya kendali utama, App bisa diibaratkan Wakil Ketua, Bendahara, Sekretaris dll yang punya fungsi masing-masing
    # Project = Webku, App = Menu, Branch, Contact
    # Cara bikin App = python manage.py startapp [nama_app]
    # Kenapa kita perlu bikin app, biar mudah mengorganisirnya, kayak Ketua kan ga mungkin kerja sendirian tanpa bendahara, sekretaris dll
    # Sekarang buka File urls di folder Menu
    url(r'^menu/', include('menu.urls')),
    url(r'^branch/', include('branch.urls')),
    url(r'^contact/', include('contact.urls')),
    # Sama kayak filter, tapi ini search. Kita harus nulis keyword sendiri. Kalau filter keywordnya udah ditentuin dari tombol (button) kategori yang otomatis keluar ketika nambahin data.
    url(r'^search/$', views.search, name='search'),
]
