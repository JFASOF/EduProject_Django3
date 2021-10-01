from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    #return HttpResponse("<h1>Index 10</h1>")
    #templates içindeki indexi render eder.
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')