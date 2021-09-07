import json

from django.http import HttpResponse, HttpResponseGone
from django.shortcuts import render


def about(request):
    return render(request, "about.html")


def index(request):
    return render(request, "index.html")




def contact(request):
    return render(request, "contact.html")


def brand(request):
    return render(request, "brand.html")


def special(request):
    return render(request, "special.html")


# def sum_view(request):
#     context = {
#         'first': 1,
#         'second': 1,
#         'sum': 2
#     }
#     return render(request, 'sum.html', context)


# def sum_two_nums(request):
#     first = int(request.GET.get("first"))
#     second = int(request.GET.get("second"))
#     return HttpResponse(first + second)


