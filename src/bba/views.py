from django.shortcuts import render

def index(req):

    context ={
        'title' : 'Dept. Of BBA'
    }
    return render(req,'bba/index.html',context=context)

def list(req):

    context = {
        'title' : 'List Of Books'
    }

    return render(req,'bba/list.html',context=context)