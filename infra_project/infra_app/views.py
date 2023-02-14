from django.http import HttpResponse


def index(request):
    return HttpResponse('По-кайфу жи!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
