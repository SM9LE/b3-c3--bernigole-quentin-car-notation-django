from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, You're at cars index.")
# Create your views here.
