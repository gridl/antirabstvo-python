from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from . import models
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from users.decorators import user_is_company


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        data = request.POST
        new_user = User.objects.create_user(
            username=data['login'], 
            first_name=data['first'], 
            last_name=data['last'],
            email=data['email']
        )
        if(data['role'] == 'company'):
            group = 2
        else:
            group = 3
        new_user.set_password(data['password'])
        new_user.groups.add(group)
        new_user.profile.phone = data['phone']
        new_user.save()
        authenticated_user = authenticate(
            username=new_user.username,
            password=data['password1']
        )
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('main:index'))

    return render(request, 'users/register.html')


@login_required
def courses(request):
    return render(request, 'users/courses.html')


def profile(request, id):
    context = {'user': User.objects.get(pk=id)}
    return render(request, 'users/profile.html', context)