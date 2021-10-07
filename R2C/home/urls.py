from django.urls import path,include
from .import views
from django.conf.urls import url


urlpatterns = [   
  path('',views.homePage,name='home'),
  path('register/',views.registerPage,name='register'),
  path('login/',views.loginPage,name='login'),
  path('products/',views.medicineDashboard,name='medicineDashboard'),
  #path('medicine/',views.medicinePage,name='medicinePage'),
  url(r'^(?P<id>[\w-]+)/', views.medicinePage,name='medicinePage'),
]
