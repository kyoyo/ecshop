from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^cart/$', views.CartGoodsView.as_view(), name='cart'),
    url(r'^pay/$', views.PayDetailView.as_view(), name='pay'),
    url(r'^cart/action/$', views.CartFormView.as_view(), name='cartAction'),
    url(r'^cart/(?P<goods_id>\d+)/addToCartSuccess/$', views.AddToCartSuccessView.as_view(), name='addToCartSuccess'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
]