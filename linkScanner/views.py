from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'linkScanner/index.html')

def learn(request):
    return render(request, 'linkScanner/learn.html', {'name':'Learn'})

def report(request):
    return render(request, 'linkScanner/report.html')

def contact(request):
    return render(request, 'linkScanner/contact.html')

def about(request):
    return render(request, 'linkScanner/about.html')
