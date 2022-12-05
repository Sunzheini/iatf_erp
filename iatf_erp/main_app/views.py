from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(5)


def process_list(request):
    return HttpResponse(6)


def process_map(request):
    return HttpResponse(7)


def process_description(request, process_id):
    return HttpResponse(f"Process Description of {process_id}")
