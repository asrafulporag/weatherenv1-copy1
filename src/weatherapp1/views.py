# # weatherapp1/views.py 

# from django.shortcuts import render, HttpResponse

# def home_view(request):
#     return HttpResponse('<h1>First Django Project</h1>')

 

from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')