from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def user_login(request):
    form = UserLoginForm()

    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        return redirect("/")
    return render(request, 'main/login_page.html', {'form':form})


def user_register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        username = request.POST['login']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 and password2 and password1 == password2:
            if not MyUser.check_username(username):
                return render(request, 'main/register_page.html', {'form':form, 'lError':True})
            try:
                user = MyUser.objects.create_user(username, password1)
            except IntegrityError:
                return render(request, 'main/register_page.html', {'form':form,'lError':True})
            user.link = "accounts/user/"+username
            user.save()
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'main/register_page.html', {'form':form, 'error':True})

    return render(request, 'main/register_page.html', {'form':form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def about(request):
    return render(request, 'main/about.html')


def articles(request, page_id=1):
    ARTICLES_ON_PAGE = 15
    articles_obj = Article.objects.all().order_by("-date")[(page_id-1)*ARTICLES_ON_PAGE:page_id*ARTICLES_ON_PAGE]
    context = {'articles':articles_obj}
    return render(request, 'main/articles.html', context=context)
























# hi