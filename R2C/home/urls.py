from django.urls import path,include
from .import views
from django.conf.urls import url


urlpatterns = [   
  path('',views.homePage,name='home'),
  path('register/',views.registerPage,name='register'),
  path('login/',views.loginPage,name='login'),
  path('logout/',views.logoutUser,name='logout'),
  path('products/',views.medicineDashboard,name='medicineDashboard'),
  path('search/',views.searchResult,name='searchResult'),
  path('cart/',views.cartPage,name='cart'),
  path('checkout/',views.checkoutPage,name='checkout'),
  path('update_item/',views.updateItem,name='update_item'),
  path('process_order/',views.processOrder,name='process_order'),
  url(r'^(?P<id>[\w-]+)/', views.medicinePage,name='medicinePage')
]
