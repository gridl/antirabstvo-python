from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views import View
from users.decorators import user_is_employer
from . import models
from vacancies.forms import VacancyForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator


@login_required
@user_is_employer
def add_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.creator = request.user
            resume.save()
        return HttpResponseRedirect(reverse('vacancies:my_vacancies'))
    else:
        form = VacancyForm()
    return render(request, 'vacancies/add_vacancy.html', {'form': form})


@login_required
@user_is_employer
def my_vacancies(request):
    vacancies = models.Vacancy.objects.filter(creator=request.user)
    return render(request, 'vacancies/my_vacancies.html', {'vacancies': vacancies})


class VacancyListView(ListView):
    queryset = models.Vacancy.objects.filter(status='published')


class VacancyDetailView(DetailView):
    model = models.Vacancy


@login_required
@user_is_employer
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
