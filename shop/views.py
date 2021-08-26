import json

from django.http import HttpResponse, HttpResponseGone
from django.shortcuts import render


def about(request):
    return HttpResponse("<h2>Главная</h2>")


def index(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = json.dumps({"name": "Tom", "age": 23})
    addr = {"Абрикосовая", 23, 45}  # кортеж

    data = {"header": header,
            "langs": langs,
            "user": user,
            "address": addr}
    return render(request, "index.html", context=data)

def sum_view(request):
    context = {
        'first': 1,
        'second': 1,
        'sum': 2
    }
    return render(request, 'sum.html', context)


def sum_two_nums(request):
    first = int(request.GET.get("first"))
    second = int(request.GET.get("second"))
    return HttpResponse(first+second)


def contact(request):
    category = request.GET.get("category", "")
    return HttpResponseGone(f"<h2>Контакты {category}</h2> "
                            f"<a href='/contact/{category}/'>ссылка</a> ")
