"""iotboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
##################################
from data import views as data
from user import views as user



urlpatterns = [
    path('', data.index,name="index"),
    path('data/', data.data,name="data"),
    path('data/<pk>', data.data_detail,name="data_detail"),
    path('login/', user.login_view, name="login_view"), # login için oluşturulan url
    path('register/', user.register_view, name="register_view"), #register için oluşturulan url
    path('logout/' , user.logout_view, name="logout_view"), #rçıkış için oluşturulan url
    path('login/message.html' , user.login_view, name="login_viw"),
    path('admin/', admin.site.urls),#proje ile gelen path
]