from django.http import HttpResponse
from django.shortcuts import render

def index(req):

    context = {
        ('title':'Home')
    }
    return render (req,'cse/index.html')
