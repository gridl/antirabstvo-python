from django.db import models


class Product(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('hidden', 'Скрыто')
    )
    title = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(verbose_name="Картинка продукта", upload_to='uploads/products/images/', blank=True)
    price = models.IntegerField(verbose_name="Цена продукта")
    give_access_to = models.ForeignKey(
        'courses.Course',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Продукт даёт доступ к курсу:"
    )
    status = models.CharField(verbose_name="Статус", max_length=20, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.title


class Coupon(models.Model):
    code = models.CharField(max_length=20, verbose_name="Код купона")
    description = models.TextField(verbose_name="Описание")
    procent_num = models.IntegerField(verbose_name="Скидка в процентах")
    max_uses = models.IntegerField(verbose_name="Максимальное количество использований", null=True, blank=True)
    max_uses_for_user = models.IntegerField(verbose_name="Максимальное количество использований на пользователя", null=True, blank=True)
    coupon_date_end = models.DateField(verbose_name="Дата окончания купона", null=True, blank=True)
    products_to_use = models.ManyToManyField(
        'Product',
        null=True,
        blank=True,
        verbose_name="Скидка действует только на товары:",
        symmetrical=False
    )
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создатель")
    date_created = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.code


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Создан'),
        ('wait', 'Ожидается оплата'),
        ('cancel', 'Отменен'),
        ('success', 'Выполнен')
    )
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name="Покупатель")
    used_coupon = models.CharField(verbose_name="Использованный купон", max_length=20, null=True, blank=True)
    gift_order = models.BooleanField(default=False, verbose_name="Курс в подарок")
    to_email = models.CharField(verbose_name="Емейл получателя купона", max_length=100, blank=True, null=True)
    message = models.TextField(verbose_name="Сообщение получателю купона", blank=True, null=True)
    products = models.ManyToManyField(Product)
    order_summ = models.IntegerField(verbose_name="Сумма заказа")
    status = models.CharField(verbose_name="Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    date_created = models.DateField(auto_now_add=True, editable=False)
