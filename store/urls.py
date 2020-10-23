from django.urls import path 
from store.views import (
    store,
    cart,
    checkout,
    login,
    register

)

urlpatterns = [
    
    path('',store, name = "store"),
    path('cart/',cart, name = "cart"),
    path('checkout/',checkout, name = "checkout")
    path('login/', login, name= 'login')
    path('register/', register, name= 'register')
]
