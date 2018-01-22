from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^all/$', views.all_questions, name='all_questions'),
    url(r'^add-question/$', views.add_question, name='add_question'),
    url(r'^question/(?P<pk>[0-9]+)/', views.view_question, name='view_question'),
    url(r'^answer/(?P<pk>[0-9]+)/', views.answer_question, name='answer_question'),
    url(r'^delete-question/(?P<pk>[0-9]+)/', views.delete_question, name='delete_question'),
    url(r'^category/(?P<category>[a-z]+)/', views.show_category, name='show_category')
]