from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm, CustomerForm

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from serpapi import GoogleSearch

# Create your views here.
def homePage(request):
  return render(request,'home/homepage.html')

def medicineDashboard(request):
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
  context = {'page_obj': page_obj,'images': img}  
  return render(request,'home/medicine_dashboard.html', context)
  
def medicinePage(request,id):
    medPage = Medicine.objects.get(id=id)
    return render(request, 'home/medicine_page.html', {'med': medPage})

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
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request,username=username, password=password)
    if user is not None:
      print('hi')
      login(request,user)
      return redirect('register')
    else:
      print('dishant mc')
      messages.info(request,'Username or password is incorrect')
      return render(request,'home/login.html')  

  context = {}
  return render(request,'home/login.html',context)

def customerDashboard(request,pk):
  customer = Customer.objects.get(id=pk)
