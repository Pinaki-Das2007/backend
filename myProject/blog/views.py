from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my blog!")


def about(request):
    a = 10+50
    return HttpResponse(f"About page! The result of the addition is: {a}")


def contact(request):
    return HttpResponse("Contact page!")