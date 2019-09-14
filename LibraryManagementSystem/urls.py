from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

urlpatterns = {
    path('admin/', admin.site.urls),
    path('cse/',include('cse.urls')),
    path('eee/',include('eee.urls'))

}
