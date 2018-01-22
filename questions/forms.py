from django.forms import ModelForm
from questions.models import Question, Answer


class QuestionAuthorizedForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'question_text',
            'visible_status',
            'category',
        ]


class QuestionUnauthorizedForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'question_text',
            'visible_status',
            'category',
            'user_name',
            'user_email'
        ]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer_text'
        ]
