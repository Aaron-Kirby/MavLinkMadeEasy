from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User
from .models import DegreePath
from .models import Courses

def firstPage(request):
    return render(request, 'landing/firstPage.html')
    
    



