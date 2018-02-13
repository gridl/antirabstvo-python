from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.ProductDetailView.as_view(), name='view_product'),
    url(r'^add-to-cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart/$', views.display_cart, name='cart'),
    url(r'^remove-from-cart/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^add-coupon/$', views.add_coupon, name='add_coupon'),
    url(r'^checkout/$', views.checkout, name='checkout')
]
