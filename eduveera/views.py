from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')