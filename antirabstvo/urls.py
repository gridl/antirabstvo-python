"""antirabstvo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from news import views as news_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', news_views.NewsListView.as_view(), name='index'),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^resumes/', include('resumes.urls', namespace='resumes')),
    url(r'^vacancies/', include('vacancies.urls', namespace='vacancies')),
    url(r'^questions/', include('questions.urls', namespace='questions')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^products/', include('products.urls', namespace="products"))
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
