from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QuestionAuthorizedForm, QuestionUnauthorizedForm, AnswerForm


# Все вопросы
def all_questions(request):
    questions = Question.objects.all()
    if not request.user.is_staff:
        questions = questions.filter(visible_status='all')
    return render(
        request,
        'questions/all.html',
        {
            'questions': questions
        }
    )


# Вопросы в определенной категории
def show_category(request, category):
    questions = Question.objects.filter(category=category)
    if not request.user.is_staff:
        questions = questions.filter(visible_status='all')
    return render(request, 'questions/all.html', {'questions': questions})


# Показать страницу вопроса
def view_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(to_question=question)
    form = AnswerForm()
    return render(
        request,
        'questions/detail.html',
        {
            'question': question,
            'answers': answers,
            'form': form
        })


# Ответ на вопрос
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.to_question = question
            answer.save()
    return HttpResponseRedirect(reverse('questions:view_question', kwargs={'pk': pk}))


# Добавить новый вопрос
def add_question(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = QuestionAuthorizedForm(request.POST)
        else:
            form = QuestionUnauthorizedForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if request.user.is_authenticated():
                question.creator = request.user
            question.save()
            return HttpResponseRedirect(reverse('questions:all_questions'))
    else:
        if request.user.is_authenticated():
            form = QuestionAuthorizedForm()
        else:
            form = QuestionUnauthorizedForm()
    return render(request, 'questions/add_question.html', {'form': form})


# Удаление вопроса
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return HttpResponseRedirect(reverse('questions:all_questions'))
