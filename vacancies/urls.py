from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add-vacancy/$', views.add_vacancy, name='add_vacancy'),
    url(r'^my-vacancies/$', views.my_vacancies, name='my_vacancies'), 
    url(r'^all/$', views.all_vacancies, name='all_vacancies')
]