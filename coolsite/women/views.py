from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Страница приложения women")


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