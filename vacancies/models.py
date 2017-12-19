from django.db import models
from users.models import User


class Vacancy(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('hidden', 'Скрыто')
    )
    title = models.CharField(verbose_name="Заголовок вакансии", max_length=255)
    location = models.CharField(verbose_name="Местоположение", max_length=255, blank=True)
    type = models.CharField(verbose_name="Тип вакансии", max_length=100, choices=(
        ('Удаленная', 'Удаленная'),
        ('Постоянная', 'Постоянная'),
        ('Проектная', 'Проектная')
    ))
    email_for_resume = models.EmailField(max_length=100)
    description = models.TextField(verbose_name="Описание вакансии")
    company_name = models.CharField(verbose_name="Название компании", max_length=100)
    company_site = models.CharField(verbose_name="Сайт компании", max_length=100)
    company_logo = models.ImageField(verbose_name="Лого компании", upload_to='uploads/companies/photo/', blank=True)
    status = models.CharField(verbose_name="Статус", max_length=20, choices=STATUS_CHOICES, default='published')
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Создатель")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/vacancies/vacancy/%i/" % self.pk


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True
    )
    company_name = models.CharField(verbose_name="Название компании", max_length=100)
    company_site = models.CharField(verbose_name="Сайт компании", max_length=100)
    company_logo = models.ImageField(verbose_name="Лого компании", upload_to='uploads/companies/photo/', blank=True)

    def __str__(self):
        return self.company_name