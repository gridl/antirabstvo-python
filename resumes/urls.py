from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^add-resume/$', views.AddResumeView.as_view(), name='add_resume'),
    url(r'^my-resumes/$', views.MyResumesView.as_view(), name='my_resumes'),
    url(r'^resume/(?P<pk>[0-9]+)/', views.ResumeDetailView.as_view(), name='view_resume'),
    url(r'^all-resumes/$', views.ResumeListView.as_view(), name='all_resumes'),
    url(r'^delete-resume/', views.DeleteResumeView.as_view(), name='delete_resume'),
    url(r'^set-resume-status/', views.SetStatusView.as_view(), name='set_status'),
    url(r'^update-resume/(?P<pk>[0-9]+)/', views.ResumeUpdateView.as_view(), name='change_resume')
]