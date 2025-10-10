from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse('Exercise every day.')

def february(request):
    return HttpResponse('Read a book every day.')