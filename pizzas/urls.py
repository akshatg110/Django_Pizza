"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import acceptorder,declineorder,adminorder,userorders,placeorder,userlogout,userauthenticate,customerwelcomeview,userloginview,signupuser,homepageview,deletepizza,addpizza,logoutadmin,adminloginview,adminhomepageview,authenticateadmin

urlpatterns = [
    path('',homepageview,name="homepage"),
    path('admin/', adminloginview, name='adminloginpage'),
    path('authenticate/',authenticateadmin),
    path('adminlogout/',logoutadmin),
    path('admin/hompepage', adminhomepageview, name='adminhomepage'),
    path('addpizza/',addpizza),
    path('deletepizza/,<int:pizzapk>/',deletepizza),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview, name='userloginpage'),
    path('customer/welcome/',customerwelcomeview,name = 'customerpage'),
    path('custauthenticate/',userauthenticate),
    path('userlogout/',userlogout),
    path('placeorder/',placeorder),
    path('userorders/',userorders),
    path('adminorderrequest/',adminorder),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder)
]
