from django.contrib import admin
from django.urls import path,include

urlpatterns = {
    path('admin/', admin.site.urls),
    path('cse/',include('cse.urls')),
    path('eee/',include('eee.urls')),
    path('bba/',include('bba.urls'))

}
