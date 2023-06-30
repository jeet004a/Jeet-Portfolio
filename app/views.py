from django.shortcuts import render,HttpResponse
from .models import Feedback
# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST.get("name", "")
        print("Name is "+name)
        obj=Feedback(name=name)
        obj.save()
    return render(request,'index.html')