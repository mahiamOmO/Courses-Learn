from django.shortcuts import render
from django.http import HttpResponse

# E:\pp\phitron\phitron-web-dev\django\templates
def index(request):
    return render(request,'index.html')

