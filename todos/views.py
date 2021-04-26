from django.shortcuts import render

# Create your views here.

def home_page(request):
    context={}
    template = 'webpages/home.html'
    return render(request,template,context)