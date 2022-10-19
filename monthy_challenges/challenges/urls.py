from django.urls import path

# To import all the fn in views.py
from . import views

# When a request reaches january execute index fn
# Here we are pointing to the function
urlpatterns = [

    path("",views.index, name="index"), #challenge/,
    path("<int:month>",views.monthly_challenge_int),
    path("<str:month>",views.monthly_challenge,name="month-challenge"),
]

# Now we need to config urls which should be triggered for the incoming request