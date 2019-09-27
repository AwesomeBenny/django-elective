from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request,
            username=request.POST['user'],
            password=request.POST['password'])
        if user:
            dj_login(request, user)
            context = {'user':request.POST['user']}
            return HttpResponseRedirect(reverse('todoapp:index'))
        else:
            context = {'error':'Username or password is wrong.'}

    return render(request, 'usersapp/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('usersapp:login'))


def signup(request):
    pass


def password_reset(request):
    pass