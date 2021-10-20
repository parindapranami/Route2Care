from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm, CustomerForm
from .utils import *
import json
import datetime

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from serpapi import GoogleSearch

# Create your views here.
def homePage(request):
  data = cartData(request)
  cartItems = data['cartItems']

  context = {'cartItems':cartItems}
  return render(request,'home/homepage.html',context)

def medicineDashboard(request):
  data = cartData(request)
  cartItems = data['cartItems']
  m = Medicine.objects.all()
  p = Paginator(m,12)
  page_number = request.GET.get('page')
  try:
    page_obj = p.get_page(page_number)
  except PageNotAnInteger:     
    page_obj = p.page(1)
  except EmptyPage:
    page_obj = p.page(p.num_pages)
  
  params = {
    "engine": "google",
    "q": "Azax 500 Tablet",
    "api_key": "7824c1c8775fbd52fdb353d265176f682f024da49e3ca0998bbcdc68cf981f30",
    "tbm" : "isch",
    "ijn" : 0,
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  # print(results)
  img = results['images_results'][0]['original']
  print(img)
  img = "https://onemg.gumlet.io/image/upload/l_watermark_346,w_480,h_480/a_ignore,w_480,h_480,c_fit,q_auto,f_auto/v1600083083/cropped/ahmbxmi2bd1wiojpxqld.jpg"
  context = {'page_obj': page_obj,'images': img,'cartItems':cartItems}  
  return render(request,'home/medicine_dashboard.html', context)
  
def medicinePage(request,id):
  data = cartData(request)
  cartItems = data['cartItems']

  medPage = Medicine.objects.get(id=id)
  context = {'med': medPage,'cartItems':cartItems}

  if request.method=='POST':
    pres = request.FILES.get('pres')
    med = medPage.med_name
    customer = request.user
    file = Prescription.objects.create(med=med,pres=pres) #,customer=customer
    file.save()
    print(file)
    
  return render(request, 'home/medicine_page.html', context)


  
 


def searchResult(request):
  s=request.GET['search']
  m = Medicine.objects.filter(med_name__icontains=s)
  return render(request,'home/search_results.html', {"meds": m})

def registerPage(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,'Account was created for ' + username)
      return redirect('login')
  
  context = {'form':form}
  return render(request,'home/register1.html',context)

def loginPage(request):
  print('shubh')
  if request.method == 'POST':
    print('parinda')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request,username=username, password=password)
    if user is not None:
      print('manasi')
      login(request,user)
      return redirect('home')
    else:
      print('mehta')
      messages.info(request,'Username or password is incorrect')
      return render(request,'home/login.html')  

  context = {}
  return render(request,'home/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# def customerDashboard(request,pk):
#   customer = Customer.objects.get(id=pk)
def cartPage(request):
  data = cartData(request)
  cartItems = data['cartItems']
  order = data['order']
  items = data['items']

  context = {'items':items,'order':order,'cartItems':cartItems}
  return render(request, 'home/cart.html',context)
  # return render(request,'home/cart.html')

# @csrf_exempt
def checkoutPage(request):
  data = cartData(request)
  cartItems = data['cartItems']
  order = data['order']
  items = data['items']
  
  context = {'items':items,'order':order,'cartItems':cartItems}
  return render(request, 'home/checkout.html',context)
  # return render(request, 'home/checkout.html')

def updateItem(request):
  data = json.loads(request.body)
  medicineId = data['medicineId']
  action = data['action']

  print('Action:',action)
  print('medicineId:',medicineId)

  customer = request.user.customer
  medicine = Medicine.objects.get(id=medicineId)
  order, created = Order.objects.get_or_create(customer=customer, complete=False)

  orderItem, created = OrderItem.objects.get_or_create(order=order, medicine=medicine)

  if action == 'add':
    orderItem.quantity = (orderItem.quantity + 1)
  elif action == 'remove':
    orderItem.quantity = (orderItem.quantity - 1)
  
  orderItem.save()

  if orderItem.quantity <= 0:
    orderItem.delete()

  return JsonResponse('Item was added',safe=False)

# @csrf_exempt
def processOrder(request):
  # print('Data:',request.body)
  print('transaction')
  transaction_id = datetime.datetime.now().timestamp()
  data = json.loads(request.body)

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

  else:
    customer, order = guestOrder(request, data)

  total = float(data['form']['total'])
  order.transaction_id = transaction_id

  if total == order.get_cart_total:
    order.complete = True
    print('order')
  order.save()

  if order.shipping == True:
    ShippingAddress.objects.create(
      customer = customer,
      order = order,
      address = data['shipping']['address'],
      city = data['shipping']['city'],
      state = data['shipping']['state'],
      # country = data['shipping']['country'],
      zipcode = data['shipping']['zipcode'],
    )

  return JsonResponse('Payment submitted...',safe=False)
