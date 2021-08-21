from django.http import HttpResponse, HttpResponseNotFound, HttpResponseGone


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def sum_two_nums(request):
    return HttpResponse("сумма чисел < число >, < число > = <сумма> ")


def contact(request):
    category = request.GET.get("category", "")
    return HttpResponseGone(f"<h2>Контакты {category}</h2> "
                            f"<a href='/contact/{category}/'>ссылка</a> ")
