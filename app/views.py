from django.shortcuts import render,HttpResponse
from .models import Feedback
# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get("name", "")
        email=request.POST.get("email","")
        text=request.POST.get("text","")
        print("Name is "+name)
        obj=Feedback(name=name,email=email,text=text)
        obj.save()
    return render(request,'index.html')