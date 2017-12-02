from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^profile/(?P<id>[0-9]+)/', views.profile, name='profile'),
    url(r'^add-vacancy/$', views.add_vacancy, name='add_vacancy'),
    url(r'^add-resume/$', views.add_resume, name='add_resume'),
    url(r'^my-resumes/$', views.my_resumes, name='my_resumes'),
    url(r'^my-vacancies/$', views.my_vacancies, name='my_vacancies'),
    url(r'^all-resumes/$', views.all_resumes, name='all_resumes')
]