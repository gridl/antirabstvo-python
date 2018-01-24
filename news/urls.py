from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/(?P<pk>[0-9]+)/', views.NewsDetailView.as_view(), name='view_news'),
    url(r'^/$', views.NewsListView.as_view(), name='all_news'),
]
