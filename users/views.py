from .models import User
from .forms import UserCreationForm
from users.decorators import user_is_employer
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data.get('role') == 'company':
                is_employer = True
            else:
                is_employer = False
            user = form.save()
            user.is_employer = is_employer
            user.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
        
    return render(request, 'users/register.html', {'form': form})


@login_required
def courses(request):
    return render(request, 'users/courses.html')


def profile(request, id):
    context = {'user': User.objects.get(pk=id)}
    return render(request, 'users/profile.html', context)