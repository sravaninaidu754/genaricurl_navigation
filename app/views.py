from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def wish(request):
    return render(request,'wish.html') 