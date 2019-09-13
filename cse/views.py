from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This Is The Department Of CSE</h1>')
