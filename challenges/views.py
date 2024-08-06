from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Veggies"
    else:
        return HttpResponseNotFound("This month isn't supported")
    return HttpResponse(challenge_text)
