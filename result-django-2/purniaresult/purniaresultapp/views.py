from django.shortcuts import render,redirect


# Create your views here.

def home(req):
    return render(req,"index.html")

def insert(req):
    return render(req,"insert.html")