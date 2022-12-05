from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(5)


def process_list(request):
    return HttpResponse(6)


def process_map(request):
    return HttpResponse(7)


def process_description(request, process_id):
    context = {
        'process_id': process_id,
        'my_info': [1, 2, 3],
    }
    return render(request, 'base.html', context)


