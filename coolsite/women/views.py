from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Women.objects.all()
    return render(request, "women/index.html",
                  {'menu': menu,
                  'posts': posts,
                  'title': 'Главная страница',
                  })


def about(request):
    return render(request, "women/about.html", {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if print(request.GET):    
        print(request.GET)
    return HttpResponse(f'<h1>Статья по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')