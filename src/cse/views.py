from django.shortcuts import render

def index(req):

    context = {
        'title':'Dept. Of CSE'
    }
    return render (req,'cse/index.html',context=context)

def list(req):

    context = {
            'title' : 'List Of Books'
    }
    return render (req,'cse/list.html',context=context)