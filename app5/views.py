from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def saimani(request):
    return HttpResponse("<h1><i><marquee>Hi This Is Me</h1></i></marquee>")