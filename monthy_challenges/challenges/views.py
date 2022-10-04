from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# The argument will be passed automatically into this function when it's executed
# This fn will not ne executed by us, instead we will soon make django aware of this fn and django will execute this fn for us when an incoming request hits django's server and is forwarded to this fn
# We will receive http request and return http response
def index(request):
    # return the response which we need to send back to the client
    return HttpResponse("This works")
# Now we need to tell django when should we call this fn, ir for which url request. So we create urls.py
