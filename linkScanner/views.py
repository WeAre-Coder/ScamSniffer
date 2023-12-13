from django.shortcuts import render
from .models import Link
from .forms import LinkForm
from linkScanner import scanner

# Create your views here.
def home(request):
    link_list = Link.objects.all()
    if request.method == 'POST':
        link = request.POST.get('link','')        
        result = scanner.check(str(link))
        status = request.POST.get('status',result)
        link = Link(link=link, status=status) #creating link object so that it gets saved in the database
        link.save()
        target_url = request.POST.get('link')   
        return render(request,'linkScanner/result.html',{'result':result, 'target_url': target_url})
    return render(request,'linkScanner/index.html',{'link_list':link_list})

def learn(request):
    return render(request, 'linkScanner/learn.html')

def report(request):
    return render(request, 'linkScanner/report.html')

def contact(request):
    return render(request, 'linkScanner/contact.html')

def about(request):
    return render(request, 'linkScanner/about.html')

def result(request):
    return render(request,'linkScanner/result.html')
