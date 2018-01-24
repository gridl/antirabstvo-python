from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . import models


class NewsListView(ListView):
    queryset = models.News.objects.filter(status='published')


class NewsDetailView(DetailView):
    model = models.News

    def get_object(self, queryset=None):
        obj = super(NewsDetailView, self).get_object(queryset=queryset)
        obj.count_views = obj.count_views + 1
        obj.save()
        return obj

