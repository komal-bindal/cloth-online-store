from django.http import HttpResponse
from django.shortcuts import render

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')