from django.contrib import admin
from django.urls import path,include

#admin - r2cadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
