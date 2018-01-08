from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add-vacancy/$', views.AddVacancyView.as_view(), name='add_vacancy'),
    url(r'^my-vacancies/$', views.MyVacanciesView.as_view(), name='my_vacancies'),
    url(r'^vacancy/(?P<pk>[0-9]+)/', views.VacancyDetailView.as_view(), name='view_vacancy'),
    url(r'^update-vacancy/(?P<pk>[0-9]+)/', views.VacancyUpdateView.as_view(), name='change_vacancy'),
    url(r'^delete-resume/', views.DeleteVacancyView.as_view(), name='delete_vacancy'),
    url(r'^all-vacancies/$', views.VacancyListView.as_view(), name='all_vacancies')
]