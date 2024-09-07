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
from .views import first_view,index,books_view,book_list_view,create_book_view,book_detail_view,edit_book_view,delete_book_view,my_books_view,make_order_view,my_orders
#book_detail_view,edit_book_view

urlpatterns = [
    path('first_page/', first_view, name="first_view"),
  


    path('home/',index,name='home'),
    path('books/',books_view,name='books_view'),

    # path('book_list/', book_list, name='book_list'),
    # path('create_book',create_book,name='create_book')

    path('book_list',book_list_view,name="book_list"),
    path('my-books',my_books_view,name="my_books"),

    path('my-orders',my_orders,name="my_orders"),

    

    path('create-book',create_book_view,name="create_book"),

    path('book_detail/<slug:pk>',book_detail_view,name="book_detail"),

    path('edit_book/<slug:pk>',edit_book_view,name="edit_book"),
    path('delete_book/<slug:pk>',delete_book_view,name="delete_book"),

    path("make-order/<slug:uuid>",make_order_view,name="make_order"),
    
    # path('book-detail-view/<slug:pk>',book_detail_view,name="book_detail_view"),

    # path('books-edit/<slug:pk>', edit_book_view, name='edit_book_view'),


  ]
