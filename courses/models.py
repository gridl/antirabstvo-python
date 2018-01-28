from django.db import models


class Course(models.Model):
    FOR_ROLE_CHOICES = (
        ('all', 'Для всех'),
        ('users', 'Пользователям'),
        ('companies', 'Рекрутёрам')
    )
    title = models.CharField(verbose_name="Название курса", max_length=200)
    for_role = models.CharField(verbose_name="Для кого", max_length=40, choices=FOR_ROLE_CHOICES, default='all')

    def __str__(self):
        return self.title


class CourseSection(models.Model):
    VISIBLE_CHOICES = (
        ('show', 'Пользователь видит раздел в списке разделов курса'),
        ('hide', 'Пользователь получает доступ к разделу только по ссылке'),
    )
    course_id = models.ForeignKey(
        'Course',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name="Название раздела", max_length=200)
    section_content = models.TextField(verbose_name="Содержимое раздела")
    visibility = models.CharField(verbose_name="Видимость раздела", max_length=40, choices=VISIBLE_CHOICES, default='show')

    def __str__(self):
        return self.title


class Homework(models.Model):
    section_id = models.ForeignKey(
        'CourseSection',
        on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name="Заголовок перед формой", max_length=200)
    content = models.TextField(verbose_name="Дополнительный текст перед формой", null=True, blank=True)

    def __str__(self):
        return self.title


class UserAccessToCourse(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    progress_section = models.ForeignKey('CourseSection', on_delete=models.SET_NULL, null=True, blank=True)
    date_start = models.DateField(auto_now_add=True)


class UserHomework(models.Model):
    STATUS_CHOICES = (
        ('send', 'Пользователь отправил файл'),
        ('review', 'Файл проверен куратором'),
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    file = models.FileField(verbose_name="Файл с домашним заданием", upload_to='uploads/homework/')
    status = models.CharField(verbose_name="Статус", max_length=40, choices=STATUS_CHOICES, default='send')
