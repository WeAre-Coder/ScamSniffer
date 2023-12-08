from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>WELCOME TO OUR PAGE</h1>')

def learn(request):
    return HttpResponse('LEARN MORE')

def report(request):
    return HttpResponse('Report if something wrong')
