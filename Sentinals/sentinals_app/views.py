from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def roster(request):
    return render(request, 'roster.html')