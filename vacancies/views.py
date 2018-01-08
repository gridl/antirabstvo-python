from . import models
from vacancies.forms import VacancyForm
from users.decorators import user_is_employer
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_employer, name='dispatch')
class AddVacancyView(FormView):
    template_name = 'vacancies/add_vacancy.html'
    form_class = VacancyForm
    success_url = reverse_lazy('vacancies:my_vacancies')

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.creator = self.request.user
        vacancy.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_employer, name='dispatch')
class MyVacanciesView(View):
    template_name = 'vacancies/my_vacancies.html'

    def get(self, request, *args, **kwargs):
        vacancies = models.Vacancy.objects.filter(creator=request.user)
        return render(request, self.template_name, {'vacancies': vacancies})


class VacancyListView(ListView):
    queryset = models.Vacancy.objects.filter(status='published')


class VacancyDetailView(DetailView):
    model = models.Vacancy


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_employer, name='dispatch')
class DeleteVacancyView(View):
    def post(self, request, *args, **kwargs):
        vacancy = models.Vacancy.objects.get(pk=request.POST['vacancy'])
        vacancy.delete()
        return JsonResponse({
            'status': 'ok',
        })


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_employer, name='dispatch')
class VacancyUpdateView(UpdateView):
    model = models.Vacancy
    fields = ['title', 'location', 'type', 'email_for_resume', 'description']
    template_name_suffix = '_update'
