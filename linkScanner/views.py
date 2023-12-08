from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'linkScanner/index.html')

def learn(request):
    return render(request, 'linkScanner/learn.html')

def report(request):
    return render(request, 'linkScanner/report.html')

def contact(request):
    return render(request, 'linkScanner/contact.html')
