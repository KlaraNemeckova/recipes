from django.shortcuts import render
from django.http import HttpResponse


def soup(request):
    return HttpResponse("This is recipe for the chicken soup.")
