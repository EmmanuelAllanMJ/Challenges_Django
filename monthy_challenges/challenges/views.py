from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december":None,
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        # response_data = "<h1>{}<h1>".format(challenge_text)
        return render(request, "challenges/challenge.html",{
            "month":month,
            "text": challenge_text
        })
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        raise  Http404()