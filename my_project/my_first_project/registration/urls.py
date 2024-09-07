"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from .views import register, user_login, user_logout
from .views import sign_up_view,login_view,logout_view,profile_view,change_password,editProfile,user_activate_view

urlpatterns = [

    path('sign-up/',sign_up_view,name="sign_up"),
    path('sign-in',login_view,name="sign_in"),

    path('logout/', logout_view, name='logout'),

    #path('profile/', profile_view, name='profile'),
    path('editProfile',editProfile,name='editProfile'),
    path('activate/<slug:id>',user_activate_view,name="activate"),
    #path('activate/<str:uuid>',acitivate_url,name='activate'),
    path('change_password',change_password,name='change_password')
    

    # path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),


  ]
