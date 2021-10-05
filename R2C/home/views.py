from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm, CustomerForm

# Create your views here.
def homePage(request):
  return render(request,'home/homepage.html')

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
