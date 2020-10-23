from django.urls import path 
from store.views import (
    store,
    cart,
    checkout,
    login_page,
    register

)

urlpatterns = [
    
    path('',store, name = "store"),
    path('cart/',cart, name = "cart"),
    path('checkout/',checkout, name = "checkout"),
    path('login/', login_page, name= 'login'),
    path('register/', register, name= 'register')
]
