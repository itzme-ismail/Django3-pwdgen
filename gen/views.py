from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'gen/home.html')
def pwd(request):
#    char='abcdefghijklmnopqrstuvwxyz'
    char=request.GET.get('char')
    leng=int(request.GET.get('length'))
    if request.GET.get('Upper'):
        char1=char.upper()
        char=char + char1
    thepwd=''
    for x in range(leng):
        thepwd += random.choice(char)
    return render(request,'gen/pwd.html',{'password':thepwd})
def about(request):
    return render(request,'gen/about.html')

# Create your views here.
