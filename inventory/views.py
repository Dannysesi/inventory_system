from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>In index view</p>')

def item_detail(request):
    return HttpResponse('<p>in item_detail view with id</p>')

