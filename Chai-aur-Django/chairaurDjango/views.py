from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,world.you are at chai aur django home page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello,world.you are at chai aur django about page")

def contact(request):
    return HttpResponse("Hello,world.you are at chai aur django contact page")
