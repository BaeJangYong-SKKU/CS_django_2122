from django.shortcuts import render, get_object_or_404
from .models import PostNormal

# Create your views here.

def index(request):
    return render(request, 'titlep/titlep.html') #나중에 proj/main.html로 변경해야함

def list(request):
    return render(request, 'proj/list.html')