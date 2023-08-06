from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}!")

def index(request):
    return render(request, "diary/index.html")


def greet(request, name):
    return render(request, "diary/greet.html", {
        "name": name.capitalize()
    })