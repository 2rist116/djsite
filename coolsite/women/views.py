from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения women")


def categories(request):
    return HttpResponse('<h1>Статья по категориям</h1>')
