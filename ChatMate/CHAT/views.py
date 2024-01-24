from django.shortcuts import render

# Create your views here.



def index(request):
    print("start")
    return render(request,"index.html")

def register(request):
    print("start")
    return render(request,"register.html")