from django.shortcuts import render
from users.decorators import user_is_employer
from django.contrib.auth.decorators import login_required

# Create your views here.
@user_is_employer
def all_resumes(request):
    pass


# Добавление резюме, доступно для пользователя, имеющего доступ хотя бы к одному курсу
@login_required
def add_resume(request):
    pass


# Просмотр страницы со всеми резюме текущего пользователя
@login_required
def my_resumes(request):
    pass