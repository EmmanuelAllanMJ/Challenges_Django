from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    # To construct this url in more dynamic way
    # return HttpResponseRedirect("/challenges/"+redirect_month)
    
    # The second parameter will accepts any arg which is followed by it. This gets an array or list, our case has one argument
    redirect_url = reverse("month-challenge",args=[redirect_month]) # This would effectively build a path like /challenge/january
    return HttpResponseRedirect( redirect_month)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")