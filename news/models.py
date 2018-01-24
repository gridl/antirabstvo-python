from django.db import models


class News(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('hidden', 'Скрыто')
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок новости")
    text = models.TextField(verbose_name="Содержимое новости")
    image = models.ImageField(verbose_name="Картинка новости", upload_to='uploads/news/images/', blank=True)
    count_views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создатель")
    status = models.CharField(verbose_name="Статус", max_length=20, choices=STATUS_CHOICES, default='published')
    date_created = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

    def get_status_name(self):
        return self.get_status_display()
