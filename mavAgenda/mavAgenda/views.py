from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

'''
@landing send a request to render the landing.html page
@param request: generates the response
'''
def landing(request):
    return render(request, 'landing/login.html')

'''
@selectdegree send a request to render the selectdegree.html page
@param request: generates the response
'''
def selectdegree(request):
    return render(request, 'landing/selectdegree.html')
