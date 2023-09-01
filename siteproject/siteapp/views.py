from django.shortcuts import render
from django.http import HttpResponse

from . models import Place
from . models import People
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()

    return render(request,"about.html",{'result':obj,'result1':obj1})
