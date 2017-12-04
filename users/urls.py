from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^profile/(?P<id>[0-9]+)/', views.profile, name='profile'),
]