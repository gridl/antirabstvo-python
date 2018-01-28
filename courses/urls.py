from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^my/$', views.my_courses, name='my_courses'),
    url(r'^course/(?P<pk>[0-9]+)/', views.course_page, name='course_detail'),
    url(r'^section/(?P<pk>[0-9]+)/', views.section_page, name='section_detail'),
    url(r'^next-section/(?P<pk>[0-9]+)/', views.next_section, name='next_section')
]
