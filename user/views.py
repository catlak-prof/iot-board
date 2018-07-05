from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.

from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
#######




def login_view(request):
    form= LoginForm(request.POST or None)

    print("login sayfasındayız")
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        print(username)
        print(password)
        user= authenticate(username=username, password=password)
        print(user)
        login(request, user)
        # return redirect('home')
        messages.success(request,"Giriş başarılı")
        login(request,user)
        return redirect("index")
    return render(request, "login.html", {"form": form, 'title': 'Giriş Yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)

    print(form)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password) #parola şifrelenmiş

        # user.is_staff = user.is_superuser = True #admin paneline girmek için verilen yetkidir
        user.save()
        new_user = authenticate(username=user.username, password=password)
        # new_user = authenticate(username=form.cleaned_data['user'], password = form.cleaned_data['password'])
        login(request, new_user)

    #     return redirect('register.html')
    #
    # return render(request, "templates/register.html", {"form": form, 'title': 'Üye Ol'})

        return render(request, 'index.html')
    else:
        print(form.errors)
        return render(request, "register.html", locals())

##########################
    # form = RegisterForm(request.POST or None)
    # if form.is_valid():
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #
    #     newUser = User(username=username)
    #     newUser.set_password(password)
    #
    #     newUser.save()
    #     login(request, newUser)
    #     messages.info(request, "Başarıyla Kayıt Oldunuz...")
    #
    #     return redirect("index")
    # context = {
    #     "form": form
    # }
    # return render(request, "register.html", context)
#########################


def logout_view(request):
    logout(request)
    messages.success(request, "çıkış başarılı")
    return redirect('http://127.0.0.1:8000')



