from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

def landing(request):
    return render(request, 'landing/login.html')

def selectdegree(request):
    return render(request, 'landing/selectdegree.html')
