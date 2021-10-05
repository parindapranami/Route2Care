from django.urls import path,include
from .import views


urlpatterns = [   
  path('',views.homePage,name='home'),
  path('register/',views.registerPage,name='register'),
  path('login/',views.loginPage,name='login'),
  path('medicines/',views.medicineDashboard,name='medicineDashboard'),
  path('medicinePage/',views.medicinePage,name='medicinePage'),
]
