from django.http.response import HttpResponse
from django.shortcuts import render

def hello_template(request):
    return render(request, 'index.html')