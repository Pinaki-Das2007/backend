from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Welcome to the shop home page!")

def product(request):
    return HttpResponse("Product page of the shop!")