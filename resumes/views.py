from django.shortcuts import render
from users.decorators import user_is_employer
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views import View
from . import models
import json
from resumes.forms import ResumeForm
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

# Декоратор для CBV???
# @user_is_employer
class ResumeListView(ListView):
    queryset = models.Resume.objects.filter(status='published')


# Добавление резюме, доступно для пользователя, имеющего доступ хотя бы к одному курсу
@login_required
def add_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.creator = request.user
            resume.save()
        return HttpResponseRedirect(reverse('resumes:my_resumes'))
    else:
        form = ResumeForm()
    return render(request, 'resumes/add_resume.html', {'form': form})


# Просмотр страницы со всеми резюме текущего пользователя
@login_required
def my_resumes(request):
    resumes = models.Resume.objects.filter(creator=request.user)
    return render(request, 'resumes/my_resumes.html', {'resumes': resumes})


class ResumeDetailView(DetailView):
    model = models.Resume


class SetStatusView(View):
    def post(self, request, *args, **kwargs):
        print(request.body)
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

class ResumeUpdateView(UpdateView):
    model = models.Resume
    fields = ['email', 'title', 'location', 'photo', 'industry', 'summary', 'resume_file', 'skills', 'experience']
    template_name_suffix = '_update'

