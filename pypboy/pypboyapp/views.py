from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'spent/index.html')

def add_spent(request):
    return render(request, 'spent.html')