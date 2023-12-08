from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'linkScanner/index.html')

def learn(request):
    return HttpResponse('LEARN MORE')

def report(request):
    return HttpResponse('Report if something wrong')
