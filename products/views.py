from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import models
from courses import functions as cf


class ProductDetailView(DetailView):
    model = models.Product


def add_to_cart(request):
    post_data = request.POST
    order = models.Order.objects.filter(
        user=request.user,
        status='new'
    ).first() or None
    if order is None:
        order = models.Order(user=request.user, order_summ=0)
        order.save()
    product = models.Product.objects.get(pk=post_data['product_id'])
    if product in order.products.all():
        return JsonResponse({
            'status': 'error',
            'text': 'Продукт уже есть в корзине.'
        })
    order.products.add(product)
    order.order_summ += product.price
    order.save()
    return JsonResponse({
        'status': 'ok',
        'text': 'Продукт успешно добавлен в корзину.'
    })


def display_cart(request):
    cart = models.Order.objects.filter(
        user=request.user,
        status='new'
    ).first() or None
    return render(request, 'products/cart.html', {'cart': cart})


def remove_from_cart(request):
    post_data = request.POST
    order = models.Order.objects.filter(
        user=request.user,
        status='new'
    ).first() or None
    product = models.Product.objects.get(pk=post_data['product_id'])
    if product in order.products.all():
        order.products.remove(product)
        if len(order.products.all()) == 0:
            order.delete()
            return JsonResponse({
                'status': 'redirect',
                'text': 'Заказ удалён.'
            })
        else:
            recalculate_order(order)
    else:
        return JsonResponse({
            'status': 'error',
            'text': 'Данного продукта нет в вашем заказе.'
        })
    return JsonResponse({
        'status': 'ok',
        'text': 'Продукт удален из корзину.',
        'new_price': order.order_summ
    })


def checkout(request):
    order = models.Order.objects.filter(
        user=request.user,
        status='new'
    ).first()
    if order.order_summ == 0:
        for product in order.products.all():
            course = product.give_access_to
            if course is not None and cf.have_access_to_course(request.user, course) is None:
                cf.new_access_to_course(request.user, course)
    return HttpResponseRedirect(reverse('courses:my_courses'))


def recalculate_order(order):
    order.order_summ = 0
    if order.used_coupon is not None:
        coupon = models.Coupon.objects.filter(
            code=order.used_coupon
        ).first()
        for product in order.products.all():
            order.order_summ += product.price * (1 - (0.01 * coupon.procent_num))
    else:
        for product in order.products.all():
            order.order_summ += product.price
    order.save()


def add_coupon(request):
    post_data = request.POST
    order = models.Order.objects.get(pk=post_data['order_id'])
    coupon = models.Coupon.objects.filter(
        code=post_data['coupon']
    ).first() or None
    if coupon is None:
        return JsonResponse({
            'status': 'error',
            'text': 'Купона не существует.'
        })
    if order.used_coupon is None:
        order.user_coupon = coupon.code
        order.order_summ -= (order.order_summ * (0.01 * coupon.procent_num))
        order.save()
        return JsonResponse({
            'status': 'ok',
            'text': 'Купон ' + coupon.code + ' успешно добавлен к заказу.',
            'new_price': order.order_summ
        })
    else:
        return JsonResponse({
            'status': 'error',
            'text': 'Вы уже используете купон.'
        })
