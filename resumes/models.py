from django.db import models


class Resume(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('hidden', 'Скрыто')
    )
    fio = models.CharField(verbose_name="ФИО", max_length=100)
    email = models.EmailField(max_length=100)
    title = models.CharField(verbose_name="Заголовок резюме", max_length=255)
    location = models.CharField(verbose_name="Место поиска работы", max_length=255, blank=True)
    photo = models.ImageField(verbose_name="Фотография", upload_to='uploads/user_resume/photo/', blank=True)
    industry = models.CharField(verbose_name="Отрасль", max_length=100, choices=(
        ('E-commerce', 'E-commerce'),
        ('Авиация', 'Авиация')
    ))
    summary = models.TextField(verbose_name="Саммари", blank=True)
    resume_file = models.FileField(verbose_name="Файл резюме", upload_to='uploads/user_resume/')
    skills = models.TextField(verbose_name="Навыки", blank=True)
    experience = models.CharField(verbose_name="Опыт работы", max_length=20, choices=(
        ('до 1 года', 'до 1 года'),
        ('от 1-3 лет', 'от 1-3 лет'),
        ('от 3-5 лет', 'от 3-5 лет'),
        ('более 5 лет', 'более 5 лет')
    ))
    status = models.CharField(verbose_name="Статус", max_length=20, choices=STATUS_CHOICES, default='published')
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Создатель")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/resumes/resume/%i/" % self.pk

    def get_status_name(self):
        return self.get_status_display()
