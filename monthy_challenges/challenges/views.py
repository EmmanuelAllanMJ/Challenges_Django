import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_int(request,month):
    return HttpResponse(month)

def monthly_challenge(request,month):
    if month=="january":
        challenge_text = "Eat no meat for the entire month"
    elif month=="february":
        challenge_text = "Walk for at least 20 min everyday"
    elif month=="march":
        challenge_text = "Learn django at least 20 min everyday"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)