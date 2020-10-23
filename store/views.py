from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def store(request):
  context = {}
  return render(request, 'store/store.html', context)

def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)


def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)

def login_page(request):
  if request.method == "POST":
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('cart')
  context = {}
  return render(request, 'store/login.html', context)
  #7cgx2JH!9fRFRfE

def register(request):
  form = UserCreationForm()
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')

  context = {'form':form}
  
  return render(request, 'store/register.html', context)


