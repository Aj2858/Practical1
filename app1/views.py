from django.shortcuts import render

# Create your views here.

def dhoni(request):
    return render(request, 'index.html')


def dilip(request):
    return render(request, 'd.html')