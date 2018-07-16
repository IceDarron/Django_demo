import web_kmeans.kmeans_demo.kmeans_main as kmeans_main
from django.shortcuts import render


# Create your views here.

def index(request):
    kmeans_main.init()
    return render(request, 'index.html')
