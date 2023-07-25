from django.shortcuts import render

# Create your views here.

def virat(request):
    return render(request, 'virat.html')

def ajay(request):
    return render(request, 'a.html')