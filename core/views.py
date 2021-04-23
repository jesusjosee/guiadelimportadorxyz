from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'core/about.html')

def faq (request):
    return render(request, 'core/faq.html')

def come_back_soon (request):
    return render(request, 'core/vuelve-pronto.html')