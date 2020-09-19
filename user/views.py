from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .models import WebUser

# Create your views here.
def register(request):
    """
    注册，并且重定向

    Parameters
    ----------
    request
        请求对象

    Returns
    -------
        返回注册后的页面，通常注册成功会重定向到登录界面

    """
    if request.method == "GET":
        return render(request, "user/register.html", {})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # print(request.POST)
        try:
            User.objects.get(username=username)
            return render(request, "user/register.html", {"error": "抱歉，已注册该用户"})
        except Exception as e:
            user = User.objects.create_user(username=username, password=password)
            web_user = WebUser.objects.create(user=user)
            return redirect("user:login")


def login(request):
    """

    Parameters
    ----------
    request

    Returns
    -------

    """
    if request.method == "GET":
        return render(request, "user/login.html", {})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # print(request.META)
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            # print(request)
            t = redirect("user:status")
            # print(t['Set-Cookie'])
            return t
        else:
            return render(request, "user/login.html", {"error": "抱歉，登录失败"})


def logout(request):
    """

    Parameters
    ----------
    request

    Returns
    -------

    """
    if request.method == "GET":
        if request.user.is_authenticated:
            user_logout(request)
            return redirect("user:login")
        else:
            return render(request, "user/login.html", {"error": "抱歉，登录失败"})


def status(request):
    """

    Parameters
    ----------
    request

    Returns
    -------

    """
    if request.method == "GET":
        user = request.user
        if request.user.is_authenticated:
            t = render(request, "user/status.html",
                          {"user":user})
            t.set_cookie("sessionid", request.COOKIES["sessionid"], httponly=False)
            return t
        else:
            return redirect("user:login")


@login_required(login_url="/user/login")
def operation(request):
    """

    Parameters
    ----------
    request

    Returns
    -------

    """
    print(request.GET)
    print(request.COOKIES)
    username = request.GET['username']
    number = request.GET['number']

    user = None
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        print(e)
        return render(request, "user/status.html",
                      {"user": request.user, "error": "未找到该用户"})

    user.webuser.money += int(number)
    user.webuser.save()

    request.user.webuser.money -= int(number)
    request.user.webuser.save()
    # return render(request, "user/status.html",
    #               {"user": request.user, "error":"转账成功"})
    return redirect("user:status")
