from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "Hello! There will be some more things here shortly."
    )
