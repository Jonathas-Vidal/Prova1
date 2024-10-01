from django.shortcuts import render
from django.http import HttpResponse

def core():
    HttpResponse("<h1>Core</h1>")
