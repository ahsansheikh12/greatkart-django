from email import message
from django.shortcuts import render,redirect
from contact.models import ContactData
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        messagenote=request.POST['messagenote']
        en=ContactData(name=name,email=email,messagenote=messagenote)
        en.save()
        messages.success(request,'We have received your mesage we will contact you on given email address as soon as possible.Thank You!')
        return redirect('home')
    return render(request,'contact.html')    
