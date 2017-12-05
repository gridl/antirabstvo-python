from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import user_is_employer

# Create your views here.
@user_is_employer
def add_vacancy(request):
    pass


@user_is_employer
def my_vacancies(request):
    pass


def all_vacancies(request):
    pass