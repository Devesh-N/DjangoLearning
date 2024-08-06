from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def jan(request):
    return HttpResponse("Eat more veggies!")


def feb(request):
    return HttpResponse("Exercise for half an hour every day!")
