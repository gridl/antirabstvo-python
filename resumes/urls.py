from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add-resume/$', views.add_resume, name='add_resume'),
    url(r'^my-resumes/$', views.my_resumes, name='my_resumes'),
    url(r'^all-resumes/$', views.all_resumes, name='all_resumes')
]