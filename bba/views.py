from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This Is BBA Department</h1>')