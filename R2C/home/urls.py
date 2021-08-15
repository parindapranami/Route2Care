from django.urls import path,include
from .import views

_appname_ = "home"

urlpatterns = [   
  path('home/',views.home),
]
