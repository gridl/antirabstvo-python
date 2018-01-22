from django.db import models


# Create your models here.
class Question(models.Model):
    VISIBLE_CHOICES = (
        ('all', 'Видно всем'),
        ('for_admins', 'Только мне и админу')
    )
    CATEGORY_CHOICES = (
        ('general', 'Общие вопросы'),
        ('salary', 'Зарплата и социальный пакет')
    )
    title = models.CharField(verbose_name="Заголовок вопроса", max_length=200)
    question_text = models.TextField(verbose_name="Текст вопроса")
    visible_status = models.CharField(verbose_name="Видимость", max_length=40, choices=VISIBLE_CHOICES, default='all')
    category = models.CharField(verbose_name="Категория вопроса", max_length=40, choices=CATEGORY_CHOICES, default='')
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name="Создатель", blank=True, null=True)
    user_name = models.CharField(verbose_name="Ваше имя", max_length=20, blank=True, null=True)
    user_email = models.CharField(verbose_name="Ваш емейл", max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_category_name(self):
        return self.get_category_display()

    def get_visible_status_name(self):
        return self.get_visible_status_display()


class Answer(models.Model):
    to_question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="Вопрос")
    answer_text = models.TextField(verbose_name="Текст ответа")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.answer_text
