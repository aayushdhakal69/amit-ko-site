from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
from .models import Contact

def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["content"]
        
        data = Contact()
        data.name = name
        
        data.email = email
        data.content = content
    
        
        data.save()
        send_mail(
            "Hello " + name,
            "Hey Thank You! for connecting with me I will message you shortly!",
            "212amiit@gmail.com",
            [email],
            fail_silently= False
        )        
    
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")