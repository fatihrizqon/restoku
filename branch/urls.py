from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.shortcuts import render

urlpatterns = [
    url(r'^$', views.index),
]