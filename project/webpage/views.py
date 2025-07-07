from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def indix(request):
    return render(request, 'indix.html')

def contact(request):
    return render(request, 'contect.html')