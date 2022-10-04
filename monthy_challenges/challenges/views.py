import re
from turtle import forward
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {    
    "january":"Eat no meat for the entire month",
    "february": "Walk for at least 20 min everyday",
    "march":"Learn django at least 20 min everyday",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december":"december",
}

def monthly_challenge_int(request,month):
    # Here we'll get the list
    months = list(monthly_challenges.keys())
    
    if month>12:
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)

    return HttpResponse(month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")