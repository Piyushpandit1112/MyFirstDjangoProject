from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    # context={
    #     "variable1":"My name is Piyush",
    #     "variable2":"My name is Pandit"
    # }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")
    
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,address=address,phone=phone,city=city,zip=zip,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted successfully!')
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
