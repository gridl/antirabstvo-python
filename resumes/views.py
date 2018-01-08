import json
from . import models
from users.decorators import user_is_employer
from resumes.forms import ResumeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
@method_decorator(user_is_employer, name='dispatch')
class ResumeListView(ListView):
    queryset = models.Resume.objects.filter(status='published')


@method_decorator(login_required, name='dispatch')
class AddResumeView(FormView):
    template_name = 'resumes/add_resume.html'
    form_class = ResumeForm
    success_url = reverse_lazy('resumes:my_resumes')

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.creator = self.request.user
        resume.save()
        return super().form_valid(form)


# Просмотр страницы со всеми резюме текущего пользователя
@method_decorator(login_required, name='dispatch')
class MyResumesView(View):
    template_name = 'resumes/my_resumes.html'

    def get(self, request, *args, **kwargs):
        resumes = models.Resume.objects.filter(creator=request.user)
        return render(request, self.template_name, {'resumes': resumes})


@method_decorator(login_required, name='dispatch')
class ResumeDetailView(DetailView):
    model = models.Resume


class SetStatusView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        resume = models.Resume.objects.get(pk=data['resume'])
        resume.status = data['status']
        resume.save()
        return JsonResponse({
            'status': 'ok',
        })


class DeleteResumeView(View):
    def post(self, request, *args, **kwargs):
        resume = models.Resume.objects.get(pk=request.POST['resume'])
        resume.delete()
        return JsonResponse({
            'status': 'ok',
        })


@method_decorator(login_required, name='dispatch')
class ResumeUpdateView(UpdateView):
    model = models.Resume
    fields = ['email', 'title', 'location', 'photo', 'industry', 'summary', 'resume_file', 'skills', 'experience']
    template_name_suffix = '_update'

