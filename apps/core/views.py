# Create your views here.
from django.shortcuts import render
def index(request, template="core/index.html"):
    return render(request, template)
