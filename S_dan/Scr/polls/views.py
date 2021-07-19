from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "Home.html", {})


def contacts(request):
    return render(request, "contacts.html", {})


def about(request):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123
    }
    return render(request, 'about.html', {})
